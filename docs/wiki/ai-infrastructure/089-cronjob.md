# CronJob（定时任务）

> 学科：AI Infrastructure · 专题：调度与容器 · Kubernetes 与 GPU 组件行为应按部署版本验证

## 1. 核心定义

CronJob 是 Kubernetes 中按 cron 时间表达式周期性创建 Job 的控制器。CronJob 负责计划触发和并发策略，真正执行工作的是每次生成的 Job 与其 Pod。由于控制器重启、调度延迟和 missed schedule 等情况，CronJob 不提供业务层严格 exactly-once 保证，任务应具备幂等性。

## 2. 形象理解

像每天定时生成一张工作订单：钟表决定什么时候创建订单，Job 负责完成订单。如果控制中心短暂故障，恢复后可能补跑或跳过错过的时间点，因此订单处理系统需要识别重复编号。

## 3. 技术原理与核心内容

`.spec.schedule` 使用 cron 格式；`.spec.timeZone` 可明确时区（稳定自 v1.27）；`concurrencyPolicy` 为 Allow（默认并发）、Forbid（前一 Job 未完成时跳过本次）、Replace（用新 Job 替换旧 Job）。`startingDeadlineSeconds` 限制迟到多少秒仍可启动；`suspend` 暂停后续创建；成功/失败历史保留数控制清理。控制器每次 reconcile 检查上次计划时间与当前时间，若 missed schedule 超过 100 次会停止 catch-up 并报告错误。

## 4. 工程实践与设计权衡

AI 平台可用 CronJob 做每日数据校验、embedding 重建、离线评测和模型清理。时区显式设 UTC 或业务时区，选择 Forbid/Replace 前确认旧任务可否被跳过/中断；对账任务使用唯一 schedule key、数据库唯一约束或对象存储 manifest 防止重复副作用。为慢任务设置合理 startingDeadlineSeconds 与 history limits，监控 Job 迟到、失败和漏跑。

## 5. 易混概念与边界

CronJob 不是常驻 cron daemon，也不是 Job 本身；它创建 Job，不直接运行容器。Forbid 仅限制同一 CronJob 生成的 Job 互相并发，不阻止其它 CronJob 同时执行；Replace 会终止旧 Job，并不等于事务回滚。

## 6. 中等难度面试题（含参考答案）

1. **问：为什么 CronJob 的任务应设计为幂等？** 答：控制器可能因重试/故障恢复造成重复创建或 missed schedule 补跑，严格 exactly-once 不由 CronJob 保证。用唯一业务周期键、幂等写入和去重锁避免重复副作用。

2. **问：Forbid 是否能保证整个 namespace 中同一类任务不并发？** 答：不能。它只约束同一个 CronJob 创建的 Job；其它 CronJob 或手工 Job 可并发，需要共享锁或队列实现全局互斥。

## 7. 中等难度考试题（含解析）

1. **题：CronJob 每小时触发，concurrencyPolicy=Forbid，某次 Job 执行 150 分钟；这段时间内有多少个计划时点会因前一任务运行而被跳过？** 解：若按每小时整点且从启动时点开始计算，150 分钟内会遇到 **2 个整点触发**（例如 01:00、02:00）；具体是否补跑还受 startingDeadlineSeconds 和 missed schedule 规则影响。

2. **题：successfulJobsHistoryLimit=3、failedJobsHistoryLimit=2，任务历史中有 8 个成功、5 个失败 Job，清理后最多保留多少个？** 解：最多 `3+2=**5 个**` 历史 Job；该设置只约束由此 CronJob 管理的历史对象。

## 8. 权威来源与延伸阅读

- [Kubernetes CronJob](https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/)：用于核对官方 API、架构与调度语义。
- [Kubernetes Jobs](https://kubernetes.io/docs/concepts/workloads/controllers/job/)：用于核对官方 API、架构与调度语义。

> 例题数据为教学假设，未考虑集群所有控制环与异常路径。
