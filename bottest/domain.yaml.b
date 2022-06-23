# 实体
entities:
  群体:
    type: enumerate
    values:
      - value: 老年人
      - value: 孕妇
        phrases:
          - 准妈妈

# 领域专业词汇
synonyms:
  - synonym: "新冠"
    examples:
      - 新型冠状肺炎
      - COVID-19

# 表格只读
tables:
  - table: high_risk
    rows:
      - 患病群体: 老年人
        最低年龄: 60
        最高年龄: 200
        是否属于高风险: 属于
        # 列值默认text，支持image、voice等，可用于图片等回复的渲染，格式同response
        logo图片:
          image: http://图片链接
      - 患病群体: 孕妇
        最低年龄: 20
        最高年龄: 60
        是否属于高风险: 属于
        logo图片:
          image: http://图片链接
      - 患病群体: 儿童
        最低年龄: 0
        最高年龄: 18
        是否属于高风险: 属于
        logo图片:
          image: http://图片链接

# 意图
intents:
    - intent: faq|新冠症状
#      events:
#        - ENTER
#      keywords_include:  # 关键词包含
#        - 症状
#      keywords_equal:  # 关键词等于
#        - 新冠症状
      examples:
        - COVID-19会引发哪些症状

    - intent: faq_table|查询是否是新冠高危人群
      examples:
        - '[老年人]{"entity": "群体", "role": "患病群体"}是否是新冠高危人群'

#    - intent: 多媒体触发意图
#      multimedias:
#        - image
#        - video
#        - file
#        - share_link
#        - rich_text
    - intent: faq|国家环保要求
    - intent: faq|一次性餐具危害


slots:
  # faq可能用到的词槽
  患病群体:
    auto_fill: true  # entity 或者 role 同名自动填槽
  # 不指定任何mapping，代表槽不通过query填充
  风险等级:

# faqs中定义responses
faqs:
  # 推荐 response 以 utter_xxx 开头
  utter_faq|新冠症状:
    response:
      - text: 从轻症到重症。。。。。

  # 需要查表渲染答案的回复
  utter_faq_table|查询是否是新冠高危人群:
    response:
      # 单条条件查询, 必须指定返回列，对于 find_one text_code 默认值为 result
      - text: '{slot=患病群体}是{table_lookup=high_risk.findone({患病群体:{slot=患病群体}}, {是否属于高风险:1})}高风险人群'
      # and 查询 + 结果拼接, 对于 find text_code 默认值为 ", ".join(result)
      - text: '40岁以上的高风险人群是：{
      table_lookup=high_risk.find({是否属于高风险:属于, 最低年龄:{$gte: 40}}, {患病群体:1}),
      text_code=", ".join(result)}'
      # or 查询
      # sort limit skip

  # faq&responses示例
  faq_response示例:
    # FAQ 不支持顺序一条 & 仅一次
    response_mode: all  # all:依次回复全部(缺省) random:随机回复一条
    response:
      - text: 根据环保需要，不得为顾客直接提供餐具balabala
        sug_intents:  # 话术关联推荐faq
          - intent: faq|国家环保要求
      - text: 请问你是否需要一次性餐具？
        sug_intents:  # 每条话术可以关联不同的faq
          - intent: faq|国家环保要求
          - intent: faq|一次性餐具危害
      - image:
          resource_url: http://图片资源地址
      # 仅必填字段允许不写属性名
      - image: http://图片资源地址
      - voice: 'http://音频资源地址'
      - voice:
          resource_url: 'http://音频资源地址' # 必填
          recognition: '语音识别结果'
      - video:
          resource_url: http://视频资源地址 # 必填
          title: 视频标题
          thumb: http://视频缩略图资源地址
          description: 视频描述
      - file:
          resource_url: http://文件地址 # 必填
          filename: 文件名称
      - share_link:
          destination_url: http://卡片链接地址 # 必填
          title: 卡片标题
          description: 卡片描述
          cover_url: http://卡片封面资源地址
      - rich_text:
          resource_url: http://图文链接地址 # 必填

# faq的触发规则
rules:
  - rule: 触发普通的faq
    steps:
      - intent: faq 
      - action: utter_faq 

  - rule: 触发查表的faq
    condition:
       # 指定必填词槽
      - slot_was_set:
        - 患病群体: true
    steps:
      - intent: faq_table 
      - action: utter_faq_table 
