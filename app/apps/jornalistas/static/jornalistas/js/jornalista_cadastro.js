
let number_of_alert_persona_data = 0
const alert_personal_data = `
<!-- alert for personal data form -->
              <div class="container alert alert-warning  alert-dismissible fade col-md-10 mx-auto show">

                <p class="" 
                  id ="alert_cadastro">Em Dados Pessoais, marque a caixinha ao lado de cada item para selecionar os dados que deseja exibir para a comunidade do DPJB. Caso contrário, eles serão ocultados no seu perfil.
                </p>

                <button type="button" class="btn btn-close" data-bs-dismiss="alert">
                </button>
              </div>
`


function filling_personal_data() {
  if (number_of_alert_persona_data == 0) {
    let div_alert = document.createElement("div");
    div_alert.innerHTML = alert_personal_data
    login_data.append(div_alert);
    number_of_alert_persona_data+=1
  }

}

let login_data = document.getElementById("login_data");
let personal_data_= document.getElementById("personal_data");

personal_data.addEventListener("click", filling_personal_data);