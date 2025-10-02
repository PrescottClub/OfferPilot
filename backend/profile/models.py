from django.db import models
from django.conf import settings


class UserProfile(models.Model):
    """
    用户申请档案模型
    """
    REGION_CHOICES = [
        ('uk', '英国'),
        ('us', '美国'),
        ('au', '澳大利亚'),
        ('ca', '加拿大'),
        ('eu', '欧洲'),
        ('asia', '亚洲'),
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile', verbose_name='用户')
    target_regions = models.JSONField(default=list, blank=True, verbose_name='目标地区')
    target_universities = models.JSONField(default=list, blank=True, verbose_name='目标大学')
    target_majors = models.JSONField(default=list, blank=True, verbose_name='目标专业')

    # 语言成绩
    ielts_score = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True, verbose_name='雅思成绩')
    toefl_score = models.IntegerField(null=True, blank=True, verbose_name='托福成绩')
    gre_score = models.IntegerField(null=True, blank=True, verbose_name='GRE成绩')
    gmat_score = models.IntegerField(null=True, blank=True, verbose_name='GMAT成绩')

    # 学术背景
    gpa = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True, verbose_name='GPA')
    undergraduate_school = models.CharField(max_length=200, blank=True, verbose_name='本科学校')
    major = models.CharField(max_length=200, blank=True, verbose_name='本科专业')
    graduation_year = models.IntegerField(null=True, blank=True, verbose_name='毕业年份')

    # 其他信息
    work_experience = models.TextField(blank=True, verbose_name='工作经验')
    research_experience = models.TextField(blank=True, verbose_name='科研经历')
    extracurricular = models.TextField(blank=True, verbose_name='课外活动')
    awards = models.TextField(blank=True, verbose_name='获奖情况')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '用户档案'
        verbose_name_plural = '用户档案'
        db_table = 'user_profiles'

    def __str__(self):
        return f"{self.user.nickname}的档案"


class Application(models.Model):
    """
    申请记录模型
    """
    STATUS_CHOICES = [
        ('preparing', '准备中'),
        ('submitted', '已提交'),
        ('under_review', '审理中'),
        ('interview', '面试'),
        ('offer', '获得Offer'),
        ('rejected', '被拒绝'),
        ('withdrawn', '已撤回'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='applications', verbose_name='用户')
    university_name = models.CharField(max_length=200, verbose_name='大学名称')
    major_name = models.CharField(max_length=200, verbose_name='专业名称')
    degree_type = models.CharField(max_length=50, verbose_name='学位类型')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='preparing', verbose_name='申请状态')
    application_date = models.DateField(null=True, blank=True, verbose_name='申请日期')
    deadline = models.DateField(null=True, blank=True, verbose_name='截止日期')
    result_date = models.DateField(null=True, blank=True, verbose_name='结果日期')
    notes = models.TextField(blank=True, verbose_name='备注')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '申请记录'
        verbose_name_plural = '申请记录'
        db_table = 'applications'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.nickname} - {self.university_name} - {self.major_name}"
