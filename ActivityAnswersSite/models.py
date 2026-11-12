from django.db import models


#user database
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.TextField(max_length=50, blank=False, null=False)
    email = models.TextField(max_length=255, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    password = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.username + self.email

#admin database
class Admin(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    admin_level = models.TextField(max_length=30, blank=False, null=False)

    def __str__(self):
        return str(self.user_id)

#regular_user database
class RegularUser(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    reputation = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return str(self.user_id)

#game database
class Game(models.Model):
    game_id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=50, blank=False, null=False)
    platform = models.TextField(max_length=50, blank=False, null=False)
    release_year = models.SmallIntegerField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

#question database
class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    title = models.TextField(max_length=200, blank=False, null=False)
    body = models.TextField(max_length=65535, blank=False, null=False)
    status = models.TextField(max_length=20, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0, blank=False, null=False)
    dislikes = models.IntegerField(default=0, blank=False, null=False)
    views = models.IntegerField(default=0, blank=False, null=False)

    def __str__(self):
        return self.title

#answer database
class Answer(models.Model):
    answer_id = models.AutoField(primary_key=True)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=65535, blank=False, null=False)
    is_accepted = models.BooleanField(default=False, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0, blank=False, null=False)
    dislikes = models.IntegerField(default=0, blank=False, null=False)

    def __str__(self):
        return str(self.answer_id)

#comment database
class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, blank=True)
    answer_id = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True, blank=True)
    body = models.TextField(max_length=65535, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0, blank=False, null=False)
    dislikes = models.IntegerField(default=0, blank=False, null=False)

    def __str__(self):
        return str(self.comment_id)

#guide database
class Guide(models.Model):
    guide_id = models.AutoField(primary_key=True)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    title = models.TextField(max_length=200, blank=False, null=False)
    body = models.TextField(max_length=65535, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0, blank=False, null=False)

    def __str__(self):
        return self.title