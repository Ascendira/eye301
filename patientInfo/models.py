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
    diagnosis_date = models.DateTimeField(verbose_name='诊断日期', null=True, blank=True)

    def __str__(self):
        return self.name


class EyeInfo(models.Model):
    patient_id = models.CharField(max_length=255)
    eye = models.CharField(max_length=16, verbose_name='眼别')

    main_complaint = models.TextField(verbose_name='主诉', null=True, blank=True)
    tear_duration_months = models.FloatField(verbose_name='溢泪持续时间（月）', null=True, blank=True)
    tear_accompanying_symptoms = models.CharField(max_length=255, verbose_name='溢泪的伴随症状', null=True, blank=True)
    other_tear_accompanying_symptoms = models.TextField(verbose_name='溢泪的其他伴随症状', null=True, blank=True)
    previous_tear_surgery = models.TextField(verbose_name='曾行泪道手术', null=True, blank=True)
    other_previous_tear_surgery = models.TextField(verbose_name='其他曾行泪道手术', null=True, blank=True)
    ocular_disease_history = models.CharField(max_length=255, verbose_name='眼部疾病史', null=True, blank=True)

    other_ocular_disease_history = models.TextField(verbose_name='其他眼部疾病史', null=True, blank=True)

    antineoplastic_drug = models.TextField(verbose_name='抗肿瘤药', null=True, blank=True)
    preoperative_munk_score = models.IntegerField(verbose_name='术前Munk评分', null=True, blank=True)
    preoperative_discomfort_assessment = models.FloatField(verbose_name='术前不适感评估', null=True, blank=True)
    preoperative_lacq_social_impact_score = models.FloatField(verbose_name='术前Lac-Q问卷的“社会影响评分”', null=True,
                                                              blank=True)
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
    other_final_tear_duct_diagnosis_discription = models.TextField(verbose_name='其他泪道病最终诊断具体描述', null=True,
                                                                   blank=True)

    other_ocular_diseases = models.TextField(verbose_name='其他眼部疾病', null=True, blank=True)
    glaucoma_discription = models.TextField(verbose_name='青光眼具体描述', null=True, blank=True)
    uveitis_discription = models.TextField(verbose_name='色素膜炎具体描述', null=True, blank=True)
    diabetic_retinopathy_discription = models.TextField(verbose_name='糖尿病视网膜病变具体描述', null=True, blank=True)
    other_ocular_diseases_other_discription = models.TextField(verbose_name='其他眼部疾病其他具体描述', null=True,
                                                               blank=True)


class OtherInfo(models.Model):
    # 病人ID，作为与其他表关联的主键
    patient_id = models.CharField(max_length=255, primary_key=True)

    nasal_disease_history = models.TextField(verbose_name='鼻部疾病史', max_length=255, null=True, blank=True)
    nasal_tumor = models.TextField(verbose_name='鼻腔肿瘤', null=True, blank=True)
    nasal_septum_deviation = models.TextField(verbose_name='鼻中隔偏曲', null=True, blank=True)
    nasal_surgery = models.TextField(verbose_name='鼻腔手术', null=True, blank=True)

    systemic_disease_and_history = models.TextField(verbose_name='全身疾病、特殊个人史及家族史', null=True, blank=True)
    immune_system_disease = models.TextField(verbose_name='免疫系统疾病', null=True, blank=True)
    tumor = models.TextField(verbose_name='肿瘤', null=True, blank=True)
    other_info = models.TextField(verbose_name='其他', null=True, blank=True)

    nasal_endoscopy = models.TextField(verbose_name='鼻内镜检查', null=True, blank=True)

    left_nasal_cavity_occupancy = models.TextField(verbose_name='左鼻腔占位', null=True, blank=True)
    right_nasal_cavity_occupancy = models.TextField(verbose_name='右鼻腔占位', null=True, blank=True)
    other_nasal_endoscopy_info = models.TextField(verbose_name='其他', null=True, blank=True)

    other_body_or_systemic_disease = models.TextField(verbose_name='其他部位或全身疾病', null=True, blank=True)

    # imaging_data = models.TextField(verbose_name='影像数据', null=True, blank=True)
    # axis_ct = models.CharField(verbose_name='轴位CT图', max_length=255, null=True, blank=True)
    # sagittal_ct = models.CharField(verbose_name='矢状位CT图', max_length=255, null=True, blank=True)
    # coronal_ct = models.CharField(verbose_name='冠状位CT图', max_length=255, null=True, blank=True)
    axis_ct = models.BooleanField(verbose_name='轴位CT图', default=False)
    sagittal_ct = models.BooleanField(verbose_name='矢状位CT图', default=False)
    coronal_ct = models.BooleanField(verbose_name='冠状位CT图', default=False)

    # photos = models.TextField(null=True, blank=True)
    # frontal_photos = models.CharField(verbose_name='正面照', max_length=255, null=True, blank=True)
    # front_eye_photos = models.CharField(verbose_name='眼前节照', max_length=255, null=True, blank=True)
    frontal_photos = models.BooleanField(verbose_name='正面照', default=False)
    front_eye_photos = models.BooleanField(verbose_name='眼前节照', default=False)

    # pathology_report = models.CharField(verbose_name='病理报告', max_length=255, null=True, blank=True)
    pathology_report = models.BooleanField(verbose_name='病理报告', default=False)

    # other_special_imaging_data = models.TextField(null=True, blank=True)
    # intraoperative_resection = models.CharField(verbose_name='术中切除物图片', max_length=255, null=True, blank=True)
    # nasal_endoscopy_photo = models.CharField(verbose_name='鼻内镜检查图片', max_length=255, null=True, blank=True)
    # lacrimal_endoscopy_photo = models.CharField(verbose_name='泪小管内镜图片', max_length=255, null=True, blank=True)
    intraoperative_resection = models.BooleanField(verbose_name='术中切除物图片', default=False)
    nasal_endoscopy_photo = models.BooleanField(verbose_name='鼻内镜检查图片', default=False)
    lacrimal_endoscopy_photo = models.BooleanField(verbose_name='泪小管内镜图片', default=False)

    def __str__(self):
        return self.patient_id