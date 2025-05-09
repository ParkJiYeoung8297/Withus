from django.db import models

# Create your models here.
class user(models.Model):
    login_id=models.CharField(max_length=45,primary_key=True)
    nickname=models.CharField(max_length=30,unique=True)
    password=models.CharField(max_length=45)
    comment=models.CharField(max_length=45,null=True)         # 나의 한마디
    status=models.BinaryField(default=1)  # 활동 상태 [inactive,active]
    inactivate_date=models.DateTimeField(null=True)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(null=True)

    def __str__(self):
        return self.nickname

class study(models.Model):
    study_id=models.IntegerField(primary_key=True)
    manager_id=models.ForeignKey(user,on_delete=models.CASCADE)
    close_code=models.CharField(max_length=45)
    invite_code=models.CharField(max_length=45)
    penalty=models.IntegerField()
    sname=models.CharField(max_length=30)            # 스터디 이름
    explanation=models.CharField(max_length=50,null=True)      # 스터디 설명
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(null=True)
    def __str__(self):
        return self.sname

class member(models.Model):
    member_id=models.IntegerField(primary_key=True)
    study_id=models.ForeignKey(study,on_delete=models.CASCADE)
    user_id=models.ForeignKey(user,on_delete=models.CASCADE)
    fail_day=models.IntegerField(default=0)
    create_at=models.DateTimeField(auto_now_add=True) #start date
    update_at=models.DateTimeField(null=True)
    def __str__(self):
        return f'{self.user_id.nickname} - {self.study_id.sname}'

class study_transaction(models.Model):
    transaction_id=models.IntegerField(primary_key=True)
    member_id= models.ForeignKey(member,on_delete=models.CASCADE)
    status=models.BinaryField(default=0)  # 활동 상태 [fail,complete]
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(null=True)
    def __str__(self):
        return f'Transaction {self.transaction_id} - {self.status}'


class study_image(models.Model):
    image_id=models.IntegerField(primary_key=True)
    image_url=models.CharField(max_length=255) 
    transaction_id= models.ForeignKey(study_transaction,on_delete=models.CASCADE)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(null=True)
    def __str__(self):
        return f'Image {self.image_id} for Transaction {self.transaction_id.transaction_id}'

