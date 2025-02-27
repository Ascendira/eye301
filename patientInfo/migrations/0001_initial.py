# Generated by Django 5.1.1 on 2025-02-15 08:35

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BaseInfo",
            fields=[
                (
                    "patient_id",
                    models.CharField(
                        max_length=255,
                        primary_key=True,
                        serialize=False,
                        verbose_name="病人ID",
                    ),
                ),
                (
                    "hospital_number",
                    models.CharField(max_length=255, verbose_name="住院号"),
                ),
                (
                    "hospital_time",
                    models.CharField(max_length=255, verbose_name="入院时间"),
                ),
                ("name", models.CharField(max_length=255, verbose_name="姓名")),
                ("gender", models.CharField(max_length=10, verbose_name="性别")),
                ("age", models.IntegerField(null=True, verbose_name="年龄")),
                ("nation", models.CharField(max_length=255, verbose_name="民族")),
                (
                    "allergy_history",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="过敏史"
                    ),
                ),
                (
                    "other_allergy_history",
                    models.TextField(blank=True, null=True, verbose_name="其他过敏史"),
                ),
                (
                    "diagnosis_date",
                    models.DateTimeField(blank=True, null=True, verbose_name="诊断日期"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EyeInfo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("patient_id", models.CharField(max_length=255)),
                ("eye", models.CharField(max_length=16, verbose_name="眼别")),
                (
                    "main_complaint",
                    models.TextField(blank=True, null=True, verbose_name="主诉"),
                ),
                (
                    "tear_duration_months",
                    models.FloatField(blank=True, null=True, verbose_name="溢泪持续时间（月）"),
                ),
                (
                    "tear_accompanying_symptoms",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="溢泪的伴随症状"
                    ),
                ),
                (
                    "other_tear_accompanying_symptoms",
                    models.TextField(blank=True, null=True, verbose_name="溢泪的其他伴随症状"),
                ),
                (
                    "previous_tear_surgery",
                    models.TextField(blank=True, null=True, verbose_name="曾行泪道手术"),
                ),
                (
                    "other_previous_tear_surgery",
                    models.TextField(blank=True, null=True, verbose_name="其他曾行泪道手术"),
                ),
                (
                    "ocular_disease_history",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="眼部疾病史"
                    ),
                ),
                (
                    "other_ocular_disease_history",
                    models.TextField(blank=True, null=True, verbose_name="其他眼部疾病史"),
                ),
                (
                    "antineoplastic_drug",
                    models.TextField(blank=True, null=True, verbose_name="抗肿瘤药"),
                ),
                (
                    "preoperative_munk_score",
                    models.IntegerField(blank=True, null=True, verbose_name="术前Munk评分"),
                ),
                (
                    "preoperative_discomfort_assessment",
                    models.FloatField(blank=True, null=True, verbose_name="术前不适感评估"),
                ),
                (
                    "preoperative_lacq_social_impact_score",
                    models.FloatField(
                        blank=True, null=True, verbose_name="术前Lac-Q问卷的“社会影响评分”"
                    ),
                ),
                (
                    "preoperative_gbi_score",
                    models.FloatField(blank=True, null=True, verbose_name="术前(GBI)评分"),
                ),
                (
                    "preoperative_appearance_score",
                    models.FloatField(blank=True, null=True, verbose_name="术前外观评分"),
                ),
                (
                    "final_tear_duct_diagnosis",
                    models.TextField(blank=True, null=True, verbose_name="泪道病最终诊断"),
                ),
                (
                    "dacryocystitis",
                    models.TextField(blank=True, null=True, verbose_name="泪囊炎"),
                ),
                (
                    "dacryocystitis_canaliculitis",
                    models.TextField(blank=True, null=True, verbose_name="泪小管炎"),
                ),
                (
                    "lacrimal_canaliculus",
                    models.TextField(blank=True, null=True, verbose_name="泪小管"),
                ),
                (
                    "nasolacrimal_duct_fracture",
                    models.BooleanField(blank=True, null=True, verbose_name="鼻泪管骨折"),
                ),
                (
                    "nasolacrimal_duct",
                    models.TextField(blank=True, null=True, verbose_name="鼻泪管"),
                ),
                (
                    "nasolacrimal_duct_discription",
                    models.TextField(blank=True, null=True, verbose_name="鼻泪管其他描述"),
                ),
                (
                    "lacrimal_punctum",
                    models.TextField(blank=True, null=True, verbose_name="泪点"),
                ),
                (
                    "other_final_tear_duct_diagnosis",
                    models.TextField(blank=True, null=True, verbose_name="其他泪道病最终诊断"),
                ),
                (
                    "other_final_tear_duct_diagnosis_discription",
                    models.TextField(
                        blank=True, null=True, verbose_name="其他泪道病最终诊断具体描述"
                    ),
                ),
                (
                    "other_ocular_diseases",
                    models.TextField(blank=True, null=True, verbose_name="其他眼部疾病"),
                ),
                (
                    "glaucoma_discription",
                    models.TextField(blank=True, null=True, verbose_name="青光眼具体描述"),
                ),
                (
                    "uveitis_discription",
                    models.TextField(blank=True, null=True, verbose_name="色素膜炎具体描述"),
                ),
                (
                    "diabetic_retinopathy_discription",
                    models.TextField(
                        blank=True, null=True, verbose_name="糖尿病视网膜病变具体描述"
                    ),
                ),
                (
                    "other_ocular_diseases_other_discription",
                    models.TextField(
                        blank=True, null=True, verbose_name="其他眼部疾病其他具体描述"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OtherInfo",
            fields=[
                (
                    "patient_id",
                    models.CharField(max_length=255, primary_key=True, serialize=False),
                ),
                (
                    "nasal_disease_history",
                    models.TextField(
                        blank=True, max_length=255, null=True, verbose_name="鼻部疾病史"
                    ),
                ),
                (
                    "nasal_tumor",
                    models.TextField(blank=True, null=True, verbose_name="鼻腔肿瘤"),
                ),
                (
                    "nasal_septum_deviation",
                    models.TextField(blank=True, null=True, verbose_name="鼻中隔偏曲"),
                ),
                (
                    "nasal_surgery",
                    models.TextField(blank=True, null=True, verbose_name="鼻腔手术"),
                ),
                (
                    "systemic_disease_and_history",
                    models.TextField(
                        blank=True, null=True, verbose_name="全身疾病、特殊个人史及家族史"
                    ),
                ),
                (
                    "immune_system_disease",
                    models.TextField(blank=True, null=True, verbose_name="免疫系统疾病"),
                ),
                ("tumor", models.TextField(blank=True, null=True, verbose_name="肿瘤")),
                (
                    "other_info",
                    models.TextField(blank=True, null=True, verbose_name="其他"),
                ),
                (
                    "nasal_endoscopy",
                    models.TextField(blank=True, null=True, verbose_name="鼻内镜检查"),
                ),
                (
                    "left_nasal_cavity_occupancy",
                    models.TextField(blank=True, null=True, verbose_name="左鼻腔占位"),
                ),
                (
                    "right_nasal_cavity_occupancy",
                    models.TextField(blank=True, null=True, verbose_name="右鼻腔占位"),
                ),
                (
                    "other_nasal_endoscopy_info",
                    models.TextField(blank=True, null=True, verbose_name="其他"),
                ),
                (
                    "other_body_or_systemic_disease",
                    models.TextField(blank=True, null=True, verbose_name="其他部位或全身疾病"),
                ),
                ("axis_ct", models.BooleanField(default=False, verbose_name="轴位CT图")),
                (
                    "sagittal_ct",
                    models.BooleanField(default=False, verbose_name="矢状位CT图"),
                ),
                (
                    "coronal_ct",
                    models.BooleanField(default=False, verbose_name="冠状位CT图"),
                ),
                (
                    "frontal_photos",
                    models.BooleanField(default=False, verbose_name="正面照"),
                ),
                (
                    "front_eye_photos",
                    models.BooleanField(default=False, verbose_name="眼前节照"),
                ),
                (
                    "pathology_report",
                    models.BooleanField(default=False, verbose_name="病理报告"),
                ),
                (
                    "intraoperative_resection",
                    models.BooleanField(default=False, verbose_name="术中切除物图片"),
                ),
                (
                    "nasal_endoscopy_photo",
                    models.BooleanField(default=False, verbose_name="鼻内镜检查图片"),
                ),
                (
                    "lacrimal_endoscopy_photo",
                    models.BooleanField(default=False, verbose_name="泪小管内镜图片"),
                ),
            ],
        ),
    ]
