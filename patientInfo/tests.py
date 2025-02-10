from django.test import TestCase, Client
import json
from patientInfo.models import BaseInfo, EyeInfo, OtherInfo


class PatientInfoViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_add_patient_info(self):
        url = '/patientInfo/post/2022-01-01'  # 根据 URL 配置修改
        data = {
            "data": {
                "id": "patient1",
                "hospital_number": "123",
                "hospital_time": "2022-01-01",
                "name": "John Doe",
                "sex": "Male",
                "age": 30,
                "nation": "USA",
                "allergy_history": "None",
                "other_allergy_history": "None",
                "eyeInfo": [
                    {
                        "eye": "Left",
                        "main_complaint": "Redness",
                        "tear_duration": 1.0,
                        "tear_accompanying_symptoms": "None",
                        "other_tear_accompanying_symptoms": "None",
                        "previous_tear_surgery": "None",
                        "other_previous_tear_surgery": "None",
                        "ocular_disease_history": "None",
                        "other_ocular_disease_history": "None",
                        "antineoplastic_drug": "None",
                        "preoperative_munk_score": 0,
                        "preoperative_discomfort_assessment": 0.0,
                        "preoperative_lacq_social_impact_score": 0.0,
                        "preoperative_gbi_score": 0.0,
                        "preoperative_appearance_score": 0.0,
                        "final_tear_duct_diagnosis": "None",
                        "dacryocystitis": "None",
                        "dacryocystitis_canaliculitis": "None",
                        "lacrimal_canaliculus": "None",
                        "nasolacrimal_duct_fracture": False,
                        "nasolacrimal_duct": "None",
                        "lacrimal_punctum": "None",
                        "other_final_tear_duct_diagnosis": "None",
                        "other_ocular_diseases": "None"
                    }
                ],
                "otherInfo": {
                    "nasal_disease_history": "None",
                    "nasal_tumor": "None",
                    "nasal_septum_deviation": "None",
                    "nasal_surgery": "None",
                    "systemic_disease_and_history": "None",
                    "immune_system_disease": "None",
                    "tumor": "None",
                    "other_info": "None",
                    "nasal_endoscopy": "None",
                    "left_nasal_cavity_occupancy": "None",
                    "right_nasal_cavity_occupancy": "None",
                    "other_nasal_endoscopy_info": "None",
                    "other_body_or_systemic_disease": "None",
                    "imaging_data": "None",
                    "photos": "None",
                    "pathology_report": "None",
                    "other_special_imaging_data": "None"
                }
            }
        }
        response = self.client.post(url, json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['success'], True)

    def test_get_all_patient_info(self):
        # 先添加一个病人信息
        self.test_add_patient_info()

        url = '/patientInfo/get/patient1'  # 根据 URL 配置修改
        response = self.client.get(url)
        print(response.json())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['success'], True)
        self.assertEqual(response.json()['data']['patient_id'], 'patient1')

    def test_get_base_patient_info(self):
        # 先添加一个病人信息
        self.test_add_patient_info()

        url = '/patientInfo/get/base/patient1'  # 根据 URL 配置修改
        response = self.client.get(url)
        print(response.json())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['success'], True)
        self.assertEqual(response.json()['data']['patient_id'], 'patient1')

    def test_delete_patient_info(self):
        # 先添加一个病人信息
        self.test_add_patient_info()

        url = '/patientInfo/delete/patient1'  # 根据 URL 配置修改
        response = self.client.delete(url)
        print(response.json())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['success'], True)

        # 检查数据库中是否已删除
        self.assertEqual(BaseInfo.objects.filter(patient_id='patient1').count(), 0)
        self.assertEqual(EyeInfo.objects.filter(patient_id='patient1').count(), 0)
        self.assertEqual(OtherInfo.objects.filter(patient_id='patient1').count(), 0)
