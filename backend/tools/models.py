from django.db import models


class Tool(models.Model):
    """
    工具模型
    """
    CATEGORY_CHOICES = [
        ('ielts', '雅思练习'),
        ('document', '文书编辑'),
        ('qa', '问答社区'),
        ('visa', '签证指导'),
        ('interview', '面试准备'),
        ('university', '大学数据库'),
        ('other', '其他'),
    ]

    name = models.CharField(max_length=100, verbose_name='工具名称')
    description = models.TextField(blank=True, verbose_name='工具描述')
    icon = models.ImageField(upload_to='tool_icons/', blank=True, verbose_name='图标')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other', verbose_name='分类')
    is_active = models.BooleanField(default=True, verbose_name='是否启用')
    order = models.IntegerField(default=0, verbose_name='排序')
    url = models.CharField(max_length=200, blank=True, verbose_name='跳转链接')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '工具'
        verbose_name_plural = '工具'
        db_table = 'tools'
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.name


class University(models.Model):
    """
    大学数据模型
    """
    REGION_CHOICES = [
        ('uk', '英国'),
        ('us', '美国'),
        ('au', '澳大利亚'),
        ('ca', '加拿大'),
        ('eu', '欧洲'),
        ('asia', '亚洲'),
        ('other', '其他'),
    ]

    name = models.CharField(max_length=200, verbose_name='大学名称')
    name_en = models.CharField(max_length=200, blank=True, verbose_name='英文名称')
    region = models.CharField(max_length=20, choices=REGION_CHOICES, verbose_name='地区')
    country = models.CharField(max_length=50, verbose_name='国家')
    city = models.CharField(max_length=100, blank=True, verbose_name='城市')
    ranking = models.IntegerField(null=True, blank=True, verbose_name='排名')
    website = models.URLField(blank=True, verbose_name='官网')
    description = models.TextField(blank=True, verbose_name='简介')
    logo = models.ImageField(upload_to='university_logos/', blank=True, verbose_name='校徽')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '大学'
        verbose_name_plural = '大学'
        db_table = 'universities'
        ordering = ['ranking']

    def __str__(self):
        return self.name


class Major(models.Model):
    """
    专业数据模型
    """
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='majors', verbose_name='大学')
    name = models.CharField(max_length=200, verbose_name='专业名称')
    name_en = models.CharField(max_length=200, blank=True, verbose_name='英文名称')
    degree_type = models.CharField(max_length=50, verbose_name='学位类型')
    duration = models.CharField(max_length=50, blank=True, verbose_name='学制')
    tuition = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='学费')
    currency = models.CharField(max_length=10, default='USD', verbose_name='货币')
    requirements = models.TextField(blank=True, verbose_name='申请要求')
    description = models.TextField(blank=True, verbose_name='专业描述')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '专业'
        verbose_name_plural = '专业'
        db_table = 'majors'
        ordering = ['name']

    def __str__(self):
        return f"{self.university.name} - {self.name}"
