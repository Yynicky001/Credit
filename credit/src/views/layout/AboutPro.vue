<template>

            <!-- 内容显示 -->
            <div class="detail">
                <div class="text1">
                    <h2>关于项目</h2>
                    <span class="text2">
                        <p>项目集成ERP管理系统，利用多模态情绪识别、视频分析和区块链技术，革新信贷评级流程。系统在“双录”过程中实时评估情绪风险，整合财务数据提供个性化建议，并打破“数据孤岛”，提升金融服务的安全性与准确性。
                        </p>
                    </span>
                </div>

                <div class="text1">
                    <h2>技术摘要</h2>
                    <span class="text2">
                        <p>本项目的技术路线基于多模态情感识别与信贷评级系统的构建，旨在通过融合面部情绪、语音情绪以及历史信用数据来提升信贷评估的智能化水平。</p>
                    </span>
                </div>

                <div class="text1">
                    <h2>项目部署与上线</h2>
                    <span class="text2">
                        <p>· 动态调度策略:使用PaddleServing 中的 'Resource Manager' 实现模型资源的动态调度。<br>
                            · 自适应模型优化与A/B测试: 在模型上线过程中引入了自适应模型优化与A/B测试策略。<br>
                            · 跨平台部署与性能优化: 通过结合PaddleLite和TensorRT, 实现模型在移动端、边缘设备和云端的高效部署与推理加速。</p>
                    </span>
                </div>

            </div>

</template>

<script>
export default {

}
</script>

<style scoped>
    .detail {
      margin: 30px auto;
        width: 90%;
    }
    .detail h2 {
      margin-top: 16px;
        line-height: 40px;
        padding-bottom: 10px;
        border-bottom: solid #576A86;
    }
    .text1 {
      line-height: 40px;
      font-size: 16px;
      border-bottom: solid #576A86;
      color: #eeeff1;
    }
</style>
