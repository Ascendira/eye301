# Create your models here.
from django.db import models

# Create your models here.

# 定义病人基本信息表
class BaseInfo(models.Model):
    patient_id = models.CharField(primary_key=True, max_length=255, verbose_name='病人ID')
    hospital_number = models.CharField(max_length=255, verbose_name='住院号')
    hospital_time = models.CharField(max_length=255, verbose_name='入院时间')
    name = models.CharField(max_length=255, verbose_name='姓名')
    gender = models.CharField(max_length=10, verbose_name='性别')
    age = models.IntegerField(verbose_name='年龄', null=True)
    nation = models.CharField(max_length=255, verbose_name='民族')
    allergy_history = models.CharField(max_length=255, verbose_name='过敏史', null=True, blank=True)
    other_allergy_history = models.TextField(verbose_name='其他过敏史', null=True, blank=True)

    def __str__(self):
        return self.name


class EyeInfo(models.Model):
    patient_id = models.CharField(max_length=255)
    eye = models.CharField(max_length=16, verbose_name='眼别')
    # 主诉
    main_complaint = models.TextField(null=True, blank=True)
    tear_duration_months = models.FloatField(verbose_name='溢泪持续时间（月）', null=True)
    tear_accompanying_symptoms = models.CharField(max_length=255, verbose_name='溢泪的伴随症状', null=True, blank=True)
    other_tear_accompanying_symptoms = models.TextField(verbose_name='溢泪的其他伴随症状', null=True, blank=True)
    previous_tear_surgery = models.TextField(verbose_name='曾行泪道手术', null=True, blank=True)
    other_previous_tear_surgery = models.TextField(verbose_name='其他曾行泪道手术', null=True, blank=True)
    ocular_disease_history = models.CharField(max_length=255, verbose_name='眼部疾病史', null=True, blank=True)

    other_ocular_disease_history = models.TextField(verbose_name='其他眼部疾病史', null=True, blank=True)

    antineoplastic_drug = models.TextField(verbose_name='抗肿瘤药', null=True, blank=True)
    preoperative_munk_score = models.IntegerField(verbose_name='术前Munk评分', null=True, blank=True)
    preoperative_discomfort_assessment = models.FloatField(verbose_name='术前不适感评估', null=True, blank=True)
    preoperative_lacq_social_impact_score = models.FloatField(verbose_name='术前Lac-Q问卷的“社会影响评分”', null=True, blank=True)
    preoperative_gbi_score = models.FloatField(verbose_name='术前(GBI)评分', null=True, blank=True)
    preoperative_appearance_score = models.FloatField(verbose_name='术前外观评分', null=True, blank=True)
    final_tear_duct_diagnosis = models.TextField(verbose_name='泪道病最终诊断', null=True, blank=True)
    dacryocystitis = models.TextField(verbose_name='泪囊炎', null=True, blank=True)
    dacryocystitis_canaliculitis = models.TextField(verbose_name='泪小管炎', null=True, blank=True)

    lacrimal_canaliculus = models.TextField(verbose_name='泪小管', null=True, blank=True)
    nasolacrimal_duct_fracture = models.BooleanField(verbose_name='鼻泪管骨折', null=True, blank=True)

    nasolacrimal_duct = models.TextField(verbose_name='鼻泪管', null=True, blank=True)
    nasolacrimal_duct_discription = models.TextField(verbose_name='鼻泪管其他描述', null=True, blank=True)

    lacrimal_punctum = models.TextField(verbose_name='泪点', null=True, blank=True)
    other_final_tear_duct_diagnosis = models.TextField(verbose_name='其他泪道病最终诊断', null=True, blank=True)
    other_final_tear_duct_diagnosis_discription = models.TextField(verbose_name='其他泪道病最终诊断具体描述', null=True, blank=True)

    other_ocular_diseases = models.TextField(verbose_name='其他眼部疾病', null=True, blank=True)
    glaucoma_discription = models.TextField(verbose_name='青光眼具体描述', null=True, blank=True)
    uveitis_discription = models.TextField(verbose_name='色素膜炎具体描述', null=True, blank=True)
    diabetic_retinopathy_discription = models.TextField(verbose_name='糖尿病视网膜病变具体描述', null=True, blank=True)
    other_ocular_diseases_other_discription = models.TextField(verbose_name='其他眼部疾病其他具体描述', null=True, blank=True)




class OtherInfo(models.Model):
    # 病人ID，作为与其他表关联的主键
    patient_id = models.CharField(max_length=255, primary_key=True)

    # 鼻部疾病史
    nasal_disease_history = models.TextField(max_length=255, null=True, blank=True)

    # 鼻腔肿瘤
    nasal_tumor = models.TextField(null=True, blank=True)

    # 鼻中隔偏曲
    nasal_septum_deviation = models.TextField(null=True, blank=True)

    # 鼻腔手术
    nasal_surgery = models.TextField(null=True, blank=True)

    # 全身疾病、特殊个人史及家族史
    systemic_disease_and_history = models.TextField(null=True, blank=True)

    # 免疫系统疾病
    immune_system_disease = models.TextField(null=True, blank=True)

    # 肿瘤
    tumor = models.TextField(null=True, blank=True)

    # 其他
    other_info = models.TextField(null=True, blank=True)

    # 鼻内镜检查
    nasal_endoscopy = models.TextField(null=True, blank=True)

    # 左鼻腔占位
    left_nasal_cavity_occupancy = models.TextField(null=True, blank=True)

    # 右鼻腔占位
    right_nasal_cavity_occupancy = models.TextField(null=True, blank=True)

    # 其他
    other_nasal_endoscopy_info = models.TextField(null=True, blank=True)

    # 其他部位或全身疾病
    other_body_or_systemic_disease = models.TextField(null=True, blank=True)

    # 影像数据
    imaging_data = models.TextField(null=True, blank=True)

    # 正面照，眼前节照
    photos = models.TextField(null=True, blank=True)

    # 病理报告
    pathology_report = models.TextField(null=True, blank=True)

    # 其他特殊影像资料
    other_special_imaging_data = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.patient_id