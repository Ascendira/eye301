import os
from datetime import datetime
from django.utils import timezone
import json

# Create your views here.
from django.http import JsonResponse, FileResponse
from eye301 import settings
from django.shortcuts import render

# Create your views here.

from django.views import View

from patientInfo.models import BaseInfo as mBaseInfo
from patientInfo.models import EyeInfo
from patientInfo.models import OtherInfo

response_template = {
    "success": True,
    "errCode": 0,
    "data": {
    }
}

def index(request):
    return render(request,"index.html")

class PatientInfoView(View):
    def post(self, request, date):
        try:
            naive_date = datetime.strptime(date, "%Y-%m-%d-%H-%M-%S")
            diagnosis_date = timezone.make_aware(naive_date)
        except ValueError:
            return JsonResponse({'success': False, 'errCode': 400, 'message': 'Date Format Error'}, status=400)

        data = json.loads(request.body)['data']

        #try:
        if 1==1:
            patient_id=data['id']
            mBaseInfo.objects.update_or_create(
                patient_id=patient_id,
                defaults={
                    'hospital_number':data['hospital_number'],
                    'hospital_time':data['hospital_time'],
                    'name':data['name'],
                    'gender':data['sex'],
                    'age':data['age'],
                    'nation':data['nation'],
                    'allergy_history':data['allergy_history'],  # 过敏史
                    'other_allergy_history':data['other_allergy_history'],
                    'diagnosis_date': diagnosis_date
                }
            )

            for eye_data in data['eyeInfo']:
                EyeInfo.objects.update_or_create(
                    patient_id=patient_id,
                    eye=eye_data['eye'],  # 眼别
                    defaults={
                        'main_complaint':eye_data['main_complaint'],  # 主诉
                        'tear_duration_months':eye_data['tear_duration'],  # float,溢泪持续时间（月）
                        'tear_accompanying_symptoms':eye_data['tear_accompanying_symptoms'],  # 溢泪的伴随症状
                        'other_tear_accompanying_symptoms':eye_data['other_tear_accompanying_symptoms'],  # 溢泪的其他伴随症状
                        'previous_tear_surgery':eye_data['previous_tear_surgery'],  # 曾行泪道手术
                        'other_previous_tear_surgery':eye_data['other_previous_tear_surgery'],  # 其他曾行泪道手术
                        'ocular_disease_history':eye_data['ocular_disease_history'],  # 眼部疾病史
                        'other_ocular_disease_history':eye_data['other_ocular_disease_history'],  #其他眼部疾病史
                        'antineoplastic_drug':eye_data['antineoplastic_drug'],  # 抗肿瘤药
                        'preoperative_munk_score':eye_data['preoperative_munk_score'],  # int,术前Munk评分
                        'preoperative_discomfort_assessment':eye_data['preoperative_discomfort_assessment'],  # float,术前不适感评估
                        'preoperative_lacq_social_impact_score':eye_data['preoperative_lacq_social_impact_score'],
                        # float,术前Lac-Q问卷的“社会影响评分”
                        'preoperative_gbi_score':eye_data['preoperative_gbi_score'],  # float,术前(GBI)评分
                        'preoperative_appearance_score':eye_data['preoperative_appearance_score'],  # float,术前外观评分
                        'final_tear_duct_diagnosis':eye_data['final_tear_duct_diagnosis'],  # 泪道病最终诊断
                        'dacryocystitis':eye_data['dacryocystitis'],  # 泪囊炎
                        'dacryocystitis_canaliculitis':eye_data['dacryocystitis_canaliculitis'],  # 泪小管炎
                        'lacrimal_canaliculus':eye_data['lacrimal_canaliculus'],  # 泪小管
                        'nasolacrimal_duct_fracture':eye_data['nasolacrimal_duct_fracture'],  # 是鼻泪管否骨折
                        'nasolacrimal_duct':eye_data['nasolacrimal_duct'],  # 鼻泪管
                        'nasolacrimal_duct_discription':eye_data['nasolacrimal_duct_discription'], # 鼻泪管其他描述
                        'lacrimal_punctum':eye_data['lacrimal_punctum'],  # 泪点
                        'other_final_tear_duct_diagnosis':eye_data['other_final_tear_duct_diagnosis'],  # 其他泪道病最终诊断
                        'other_final_tear_duct_diagnosis_discription':eye_data['other_final_tear_duct_diagnosis_discription'],# 其他泪道病最终诊断具体描述
                        'other_ocular_diseases':eye_data['other_ocular_diseases'],  # 其他眼部疾病
                        'glaucoma_discription':eye_data['glaucoma_discription'],  # 青光眼具体描述
                        'uveitis_discription':eye_data['uveitis_discription'],  # 色素膜炎具体描述
                        'diabetic_retinopathy_discription':eye_data['diabetic_retinopathy_discription'],  # 糖尿病视网膜病变具体描述
                        'other_ocular_diseases_other_discription':eye_data['other_ocular_diseases_other_discription'],  # 其他眼部疾病其他具体描述
                    }
                )
            data=data['otherInfo']
            OtherInfo.objects.update_or_create(
                patient_id=patient_id,
                defaults={
                    'nasal_disease_history':data['nasal_disease_history'],  # 鼻部疾病史
                    'nasal_tumor':data['nasal_tumor'],  # 鼻腔肿瘤
                    'nasal_septum_deviation':data['nasal_septum_deviation'],  # 鼻中隔偏曲
                    'nasal_surgery':data['nasal_surgery'],  # 鼻腔手术
                    'systemic_disease_and_history':data['systemic_disease_and_history'],  # 全身疾病、特殊个人史及家族史
                    'immune_system_disease':data['immune_system_disease'],  # 免疫系统疾病
                    'tumor':data['tumor'],  # 肿瘤
                    'other_info':data['other_info'],  # 其他
                    'nasal_endoscopy':data['nasal_endoscopy'],  # 鼻内镜检查
                    'left_nasal_cavity_occupancy':data['left_nasal_cavity_occupancy'],  # 左鼻腔占位
                    'right_nasal_cavity_occupancy':data['right_nasal_cavity_occupancy'],  # 右鼻腔占位
                    'other_nasal_endoscopy_info':data['other_nasal_endoscopy_info'],  # 其他
                    'other_body_or_systemic_disease':data['other_body_or_systemic_disease'],  # 其他部位或全身疾病
                }
            )
        return JsonResponse(response_template)

    def get(self, request, patient_id):
        # 判断是查询全部病人信息还是查询基础信息
        if 'base' in request.path:
            return self.get_base_info(request, patient_id)
        else:
            return self.get_all_info(request, patient_id)

    def get_all_info(self, request, patient_id):
        # 查询全部病人信息
        info = mBaseInfo.objects.filter(patient_id=patient_id).values()
        if not info:
            return JsonResponse({'success': False, 'errCode': 400, 'message': 'No Patient Found'}, status=400)
        info = list(info)[0]

        eye_info = list(EyeInfo.objects.filter(patient_id=patient_id).values())
        info['eyeInfo'] = eye_info

        other_info = list(OtherInfo.objects.filter(patient_id=patient_id).values())
        info['otherInfo'] = other_info[0] if other_info else {}

        response = response_template.copy()
        response['data'] = info
        return JsonResponse(response)

    def get_base_info(self, request, patient_id):
        # 查询基础信息
        base_info = mBaseInfo.objects.filter(patient_id=patient_id).values()
        if not base_info:
            return JsonResponse({'success': False, 'errCode': 400, 'message': 'No Patient Found'}, status=400)

        response = response_template.copy()
        response['data'] = list(base_info)[0]
        return JsonResponse(response)

    def delete(self, request, patient_id):
        # 删除该病人信息
        try:
            mBaseInfo.objects.filter(patient_id=patient_id).delete()
            EyeInfo.objects.filter(patient_id=patient_id).delete()
            OtherInfo.objects.filter(patient_id=patient_id).delete()
        except Exception as e:
            return JsonResponse({'success': False, 'errCode': 500, 'message': str(e)}, status=500)

        return JsonResponse(response_template)


class PatientInfos(View):
    def get(self, request, pageNum, pageSize):
        data = mBaseInfo.objects.all().values()
        data = list(data)
        for baseinfo in data:
            patient_id = baseinfo['patient_id']
            eyeInfo = list(EyeInfo.objects.filter(patient_id=patient_id).values())
            baseinfo.update({'eyeInfo': eyeInfo})
            otherInfo = list(OtherInfo.objects.filter(patient_id=patient_id).values())
            if len(otherInfo) > 0:
                baseinfo.update({'otherInfo': otherInfo[0]})
            else:
                baseinfo.update({'otherInfo': {}})
        l = pageNum * pageSize
        r = l + pageSize
        if l >= len(data):
            return JsonResponse({'data': []})
        elif r >= len(data):
            data = data[l:len(data)]
        else:
            data = data[l:r]
        response = response_template.copy()
        response['data'] = data
        return JsonResponse(response)


class BaseInfo(View):
    def post(self, request, date):
        data = json.loads(request.body)['data']
        if mBaseInfo.objects.filter(patient_id=data['id']).exists():
            return JsonResponse({'success': False, 'errCode': 301})
        if not 'allergy_history' in data:
            data['allergy_history'] = None
            data['other_allergy_history'] = None
        elif not 'other_allergy_history' in data:
            data['other_allergy_history'] = None
        try:
            mBaseInfo.objects.create(
                patient_id=data['id'],
                hospital_number=data['hospital_number'],
                hospital_time=data['hospital_time'],
                name=data['name'],
                gender=data['sex'],
                age=data['age'],
                nation=data['nation'],
                allergy_history=data['allergy_history'],
                other_allergy_history=data['other_allergy_history'], )
        except:
            return JsonResponse({'success': False, 'errCode': 400, 'message': 'Key Fields Are Missing'}, status=400)
        return JsonResponse(response_template)

    def get(self, request, pageNum, pageSize):
        data = mBaseInfo.objects.all().order_by('-diagnosis_date').values()
        data = list(data)
        length = len(data)
        l = pageNum * pageSize
        r = l + pageSize
        if l > len(data):
            return JsonResponse({'data': []})
        elif r >= len(data):
            data = data[l:len(data)]
        else:
            data = data[l:r]
        response = {
            'success': True,
            'errCode': 0,
            'total': length,
            'data': data
        }
        return JsonResponse(response)

class Image(View):
    def post(self, request, patient_id, img_type):
        img = request.FILES.get('img')
        img_name = img.name
        from django.utils.text import get_valid_filename
        img_name = get_valid_filename(img_name)
        # 图片后缀名
        ext = os.path.splitext(img_name)[1]
        if not ext.lower() in ['.jpg', '.png', '.pdf']:
            return JsonResponse({'success': False, 'errCode': 400, 'message': 'File Type Error'}, status=400)

        # 检查病人是否存在
        try:
            other_info = OtherInfo.objects.get(patient_id=patient_id)
        except Exception as e:
            return JsonResponse({'success': False, 'errCode': 404, 'message': 'Patient Information Does Not Exist'}, status=404)

        patient_folder = os.path.join(settings.IMG_UPLOAD, patient_id)
        os.makedirs(patient_folder, exist_ok=True)

        img_name = f'{img_type}{ext}'
        img_path = os.path.join(patient_folder, img_name)

        try:
            with open(img_path, 'wb') as fp:
                for chunk in img.chunks():
                    fp.write(chunk)
        except Exception as e:
            return JsonResponse({'success': False, 'errCode': 400, 'message': str(e)}, status=400)

        if not hasattr(other_info, img_type):
            return JsonResponse({'success': False, 'errCode': 400, 'message': f'invalid img_type: {img_type}'},
                                status=400)

        setattr(other_info, img_type, True)
        other_info.save()

        return JsonResponse(response_template)

    def get(self, request, patient_id, img_type):
        try:
            other_info = OtherInfo.objects.get(patient_id=patient_id)
        except Exception as e:
            return JsonResponse({'success': False, 'errCode': 404, 'message': 'Patient Information Does Not Exist'}, status=404)

        if not hasattr(other_info, img_type):
            return JsonResponse({'success': False, 'errCode': 400, 'message': f'invalid img_type: {img_type}'},
                                status=400)

        field_value = getattr(other_info, img_type)

        if field_value:
            patient_folder = os.path.join(settings.IMG_UPLOAD, patient_id)
            base_img_name = f'{img_type}'
            extensions = ['.jpg', '.png', '.pdf']
            for ext in extensions:
                img_name = base_img_name + ext
                img_path = os.path.join(patient_folder, img_name)
                print(img_path)
                if os.path.exists(img_path):
                    return FileResponse(open(img_path, 'rb'), as_attachment=True, filename=img_name)

        return JsonResponse({'success': False, 'message': 'File does not exist'}, status=404)