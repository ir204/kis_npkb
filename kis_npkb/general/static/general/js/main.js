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

        $.ajax({
            url: "http://127.0.0.1:8000/competence-for-employee/" + employeeId,
        }).done(function(data) {
            $("#skill-or-competence-list").html( data  );
        });
    }

function showSkill(employeeId) {

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