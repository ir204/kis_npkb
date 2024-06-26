function clickOnEmployeeInList(){

            let employees = jQuery(".employee-list").click(
            function(){
                let employeeId = jQuery(this).attr("data-employeeid");
                showEmployeeDetail(employeeId);
                $("#employee-list-by-competence-or-skill").empty();
                $("#skill-or-competence-list").empty();
            }
        );
    }

function clickOnCompetenceButton(){

        let employees = jQuery(".competence-button").click(
        function(){
            let employeeId = jQuery(".detail").attr("data-employeeid");
            showCompetence(employeeId);
            $("#employee-list-by-competence-or-skill").empty();
        }
    );
}

function clickOnSkillButton(){

        let employees = jQuery(".skill-button").click(
        function(){
            let employeeId = jQuery(".detail").attr("data-employeeid");
            showSkill(employeeId);
            $("#employee-list-by-competence-or-skill").empty();
        }
    );
}


function addEventListeners(){
    clickOnEmployeeInList();
    clickOnCompetenceButton();
    clickOnSkillButton();
}

addEventListeners();