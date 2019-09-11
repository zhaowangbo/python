



import os
import json



stu_dict = {
    'Albert1': {'Chinese': 80, 'Math': 100, 'English': 95},
    'Albert2': {'Chinese': 83, 'Math': 90, 'English': 99},
    'Albert3': {'Chinese': 96, 'Math': 79, 'English': 98}
}

class StudentScore:
    def __init__(self, student_dict):
        self.student_dict = student_dict

        for name, score_dict in student_dict.items():
            with open("%s.json" % name, "w", encoding="utf-8") as f:
                json.dump(score_dict, f)
                f.flush()




    def check_all_score(self, name):
        use_path = "%s.json" % name

        if os.path.exists(use_path):
            with open(use_path, "r", encoding="utf-8") as f:
                use_dict = json.load(f)
                return use_dict
        else:
            return "there is not this student"



        # scores = self.student_dict.get(name)
        # return s


    def check_all_subject(self, subject):
        name_score_dict = {}
        path_list = os.listdir("C:/Users/赵望博/Desktop/python编程学习/python/第三阶段/第十一章类与对象")
        for name_path in path_list:
            if name_path.endswith("json"):
                with open(name_path, "r", encoding='utf-8') as f:
                    student_score_dict = json.load(f)
                    name_score_dict[name_path[:-5]] = student_score_dict.get(subject)

        return name_score_dict


        # scores = {}
        # for name, score_dict in self.student_dict.items():
        #     scores[name] = score_dict.get(subject)
        # return scores

    def check_average(self):
        scores = 0
        subject_count = 0
        path_list = os.listdir("C:/Users/赵望博/Desktop/python编程学习/python/第三阶段/第十一章类与对象")
        for name_path in path_list:
            if name_path.endswith("json"):
                with open(name_path, "r", encoding="utf-8") as f:
                    student_score_dict = json.load(f)
                    for score in student_score_dict.values():
                        scores += score
                        subject_count += 1
        return scores / subject_count

        # scores = 0
        # subject_num = 0
        #
        # for name, scores_dict in self.student_dict.items():
        #     for subject, score in scores_dict.items():
        #         scores += score
        #         subject_num += 1
        #
        # return scores / subject_num

    def check_some_score(self, name, subject):

        student_path = "%s.json" % name

        with open(student_path, "r", encoding="utf-8") as f:
            student_dict = json.load(f)
            print(student_dict)
            return student_dict.get(subject)





        # score_dict = self.student_dict.get(name)
        # score = score_dict.get(subject)
        # return score








res = StudentScore(stu_dict)
print(res.check_some_score("Albert1", "Math"))
