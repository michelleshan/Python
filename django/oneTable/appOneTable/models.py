from django.db import models

# ONE Dungeon has MANY prisoners
# ONE Prisoner has ONE Dungeon
# ONE to MANY

# ONE Dungeon has MANY dislikes
# ONE Prisoner has MANY dislikes
# MANY to MANY

class Dungeon(models.Model):
    name = models.TextField()
    num_people_inside = models.IntegerField()
    location = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Prisoner(models.Model): 
    name = models.TextField()
    dungeon_inside = models.ForeignKey(Dungeon,related_name="all_prisoners",on_delete=models.CASCADE)
    dungeons_disliked = models.ManyToManyField(Dungeon,related_name='prisoners_that_dislike')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)