function showDeputiesByCompetence(competenceId, employeeId){
       // Показать заместителей, получив идентификатор компетенции.
        $.ajax({
            url: "http://127.0.0.1:8000/employees/employees-by-competence/" + competenceId + "/" + employeeId,
        }).done(function(data) {
            $("#employee-list-by-competence-or-skill").html( data  );
            $("#employee-list-by-competence-or-skill")[0].focus();
        });
    }

function showDeputiesBySkill(skillId, employeeId){
       // Показать заместителей, получив идентификатор компетенции.
        $.ajax({
            url: "http://127.0.0.1:8000/employees/employees-by-skill/" + skillId + "/" + employeeId,
        }).done(function(data) {
            $("#employee-list-by-competence-or-skill").html( data  );
            $("#employee-list-by-competence-or-skill")[0].focus();
        });
    }

function showCompetence(employeeId) {
        // Показать компетенции сотрудника, получив идентификатор сотрудника
        $.ajax({
            url: "http://127.0.0.1:8000/employees/competence-for-employee/" + employeeId,
        }).done(function(data) {
            $("#skill-or-competence-list").html( data  );
        });
    }

function showSkill(employeeId) {
        // Показать навыки сотрудника, получив идентификатор сотрудника
        $.ajax({
            url: "http://127.0.0.1:8000/employees/skill-for-employee/" + employeeId,
        }).done(function(data) {
            $("#skill-or-competence-list").html( data  );
        });
    }

function showEmployeeDetail(employeeId){
        // Показать детальные записи о сотруднике, получив его идентификатор.
        $.ajax({
            url: "http://127.0.0.1:8000/employees/employee/" + employeeId,
        }).done(function(data) {
            $("#employee-info").html( data  );
            $(".competence-button").removeClass("visually-hidden");
            $(".skill-button").removeClass("visually-hidden");
            $("#employee-list-by-competence-or-skill").empty();
            $("#skill-or-competence-list").empty();
        });
    }


    // Для таблиц

function showEmployeesBySkill(skillId, sectorId){
       // Показать сотрудников, получив идентификатор навыка.
        $.ajax({
            url: "http://127.0.0.1:8000/skills/employees-by-skill-table/" + skillId + "/" + sectorId,
        }).done(function(data) {
            $("#employee-list-by-skill").html( data  );
        });
    }

function showEmployeesByCompetence(competenceId, sectorId){
       // Показать сотрудников, получив идентификатор компетенции.
        $.ajax({
            url: "http://127.0.0.1:8000/competences/employees-by-competence-table/" + competenceId + "/" + sectorId,
        }).done(function(data) {
            $("#employee-list-by-competence").html( data  );
        });
    }


function showEmployee(targetUrl, employeeId) {
    // Переход на другую страницу с внесением данных в куки.
        document.cookie = "employee=" + employeeId + "; Path=/; Domain=127.0.0.1";
        location.replace(targetUrl);
    }

function showEmployeeByRedirect(){
    // Получение данных из куки после перехода на страницу, с последующим их удалением.
        if ( document.cookie.split('; ').find(row => row.startsWith("employee=")) ) {
            let employeeId = document.cookie.split('; ').find(row => row.startsWith("employee="));
            employeeId = employeeId.split("employee=");
            employeeId = parseInt(employeeId[1]);
            showEmployeeDetail(employeeId);
            document.cookie = "employee=; Path=/; Domain=127.0.0.1; Max-Age= -1";
        }
    }