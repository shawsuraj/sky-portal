from django.db import models
from django.contrib.auth.models import User 

# 1. Organisation Table
# Featured on Wireframe Page 5 & 6
class Organisation(models.Model):
    org_name = models.CharField(max_length=150)

    def __str__(self):
        return self.org_name

# 2. Department Table
# Used for filtering in Wireframe Page 7
class Department(models.Model):
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE, related_name='departments')
    department_name = models.CharField(max_length=150)
    dept_description = models.TextField(blank=True, null=True)
    dept_leader_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='led_departments')
    specialisation = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.department_name

# 3. Team Table 
# The Core of Student 1 Rubric
class Team(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='teams')
    manager_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='managed_teams')
    members = models.ManyToManyField(User, related_name='teams_joined', blank=True)
    
    team_name = models.CharField(max_length=150)
    responsibilities = models.TextField(blank=True, null=True) # Used in Overview Tab
    purpose = models.TextField(blank=True, null=True)          # Used in Overview Tab
    description = models.TextField(blank=True, null=True)      # Used for Directory Cards
    status = models.CharField(max_length=50, default='Active')
    
    skills = models.CharField(max_length=255, blank=True, null=True, help_text="e.g. AWS, Django, React")
    
    created_date = models.DateTimeField(auto_now_add=True)
    disbanded_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.team_name
    
# 4. Repository Table
# Featured on Wireframe Page 8
class Repository(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='repositories')
    repo_name = models.CharField(max_length=150)
    repo_url = models.URLField(blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.repo_name} ({self.team.team_name})"

# 5. Team Dependency Table 
# Used for the "Dependency Map" in Wireframe Page 9
class TeamDependency(models.Model):
    upstream_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='downstream_dependencies')
    downstream_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='upstream_dependencies')
    
    dependency_type = models.CharField(max_length=100)
    dependency_description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.downstream_team.team_name} depends on {self.upstream_team.team_name}"