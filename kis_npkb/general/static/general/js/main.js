function showDeputiesByCompetence(competenceId, employeeId){
       // Показать заместителей, получив идентификатор компетенции.
        $.ajax({
            url: "http://127.0.0.1:8000/employees-by-competence/" + competenceId + "/" + employeeId,
        }).done(function(data) {
            $("#employee-list-by-competence-or-skill").html( data  );
        });
    }

function showDeputiesBySkill(skillId, employeeId){
       // Показать заместителей, получив идентификатор компетенции.
        $.ajax({
            url: "http://127.0.0.1:8000/employees-by-skill/" + skillId + "/" + employeeId,
        }).done(function(data) {
            $("#employee-list-by-competence-or-skill").html( data  );
        });
    }

function showCompetence(employeeId) {
        // Показать компетенции сотрудника, получив идентификатор сотрудника
        $.ajax({
            url: "http://127.0.0.1:8000/competence-for-employee/" + employeeId,
        }).done(function(data) {
            $("#skill-or-competence-list").html( data  );
        });
    }

function showSkill(employeeId) {
        // Показать навыки сотрудника, получив идентификатор сотрудника
        $.ajax({
            url: "http://127.0.0.1:8000/skill-for-employee/" + employeeId,
        }).done(function(data) {
            $("#skill-or-competence-list").html( data  );
        });
    }

function showEmployeeDetail(employeeId){
        // Показать детальные записи о сотруднике, получив его идентификатор.
        $.ajax({
            url: "http://127.0.0.1:8000/employee/" + employeeId,
        }).done(function(data) {
            $("#employee-info").html( data  );
        });
    }

    // Для таблиц

function showEmployeesBySkill(skillId, sectorId){
       // Показать сотрудников, получив идентификатор навыка.
        $.ajax({
            url: "http://127.0.0.1:8000/employees-by-skill-table/" + skillId + "/" + sectorId,
        }).done(function(data) {
            $("#employee-list-by-skill").html( data  );
        });
    }

function showEmployeesByCompetence(competenceId, sectorId){
       // Показать сотрудников, получив идентификатор компетенции.
        $.ajax({
            url: "http://127.0.0.1:8000/employees-by-competence-table/" + competenceId + "/" + sectorId,
        }).done(function(data) {
            $("#employee-list-by-competence").html( data  );
        });
    }