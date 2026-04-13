from django.db import models
from django.contrib.auth.models import User 

# 1. Organisation Table
class Organisation(models.Model):
    org_name = models.CharField(max_length=150)

    def __str__(self):
        return self.org_name

# 2. Department Table
class Department(models.Model):
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE, related_name='departments')
    department_name = models.CharField(max_length=150)
    dept_description = models.TextField(blank=True, null=True)
    dept_leader_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='led_departments')

    def __str__(self):
        return self.department_name

# 3. Team_Type Table
class TeamType(models.Model):
    type_name = models.CharField(max_length=100)
    type_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.type_name

# 4. Team Table 
class Team(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='teams')
    team_type = models.ForeignKey(TeamType, on_delete=models.SET_NULL, null=True)
    manager_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='managed_teams')
    
    team_name = models.CharField(max_length=150)
    responsibilities = models.TextField(blank=True, null=True)
    purpose = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50, default='Active')
    
    created_date = models.DateTimeField(auto_now_add=True)
    disbanded_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.team_name

# 5. TeamDependency Table 
class TeamDependency(models.Model):
    upstream_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='downstream_dependencies')
    downstream_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='upstream_dependencies')
    
    dependency_type = models.CharField(max_length=100)
    dependency_description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.downstream_team.team_name} depends on {self.upstream_team.team_name}"