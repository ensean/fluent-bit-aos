### 使用fluent-bit 及 Kinesis 服务将日志推送至OpenSearch

#### 使用fluent-bit + Kinesis firehose

* fluent-bit 配置参考 fluent-bit-sample.conf (通过环境变量配置ak、sk权限)
* 其余参考此[workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/32e6bc9a-5c03-416d-be7c-4d29f40e55c4/en-US/lab-4/lab4-1-os)

#### 使用fluent-bit + Kinesis data streams + lambda

* 参考代码 `sample.py`

* 注意事项
    * requests 可通过Lambda layer添加依赖（推荐使用12及以下版本，过高版本会导致urlib3 ssl不兼容错误），layer arn可以在[这里](https://api.klayers.cloud/api/v2/p3.8/layers/latest/ap-northeast-1/html)查询
    * Lambda 需要开启VPC，能够通过VPC访问AOS
    * Lambda 角色需要有权限读取Kinesis data streams