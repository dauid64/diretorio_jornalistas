$(function() {
    $('.mask-cpf').mask('000.000.000-00', {reverse: true});

    $('form').submit(function() {
        // Atualiza o valor do campo sem as mascaras
        $('.mask-cpf').unmask();
    })
});


const input = document.querySelector(".mask-phone-international");
const errorMsg = document.querySelector("#error-msg");
const validMsg = document.querySelector("#valid-msg");

const errorMap = ["Número inválido", "Código do país inválido", "Muito curto", "Muito longo", "Número Inválido"];

const iti = window.intlTelInput(input, {
initialCountry: 'BR',
separateDialCode: true,
utilsScript: "https://cdn.jsdelivr.net/npm/intl-tel-input@18.2.1/build/js/utils.js",
});

const reset = () => {
input.classList.remove("error");
errorMsg.innerHTML = "";
errorMsg.classList.add("hide");
validMsg.classList.add("hide");
};

input.addEventListener('blur', () => {
reset();
if (input.value.trim()) {
    if (iti.isPossibleNumber()) {
    validMsg.classList.remove("hide");
    } else {
    input.classList.add("error");
    const errorCode = iti.getValidationError();
    errorMsg.innerHTML = errorMap[errorCode];
    errorMsg.classList.remove("hide");
    }
}
});

// on keyup / change flag: reset
input.addEventListener('change', reset);
input.addEventListener('keyup', reset);

$('form').submit(function() {
    // Atualiza o valor do campo sem as mascaras
    input.value = iti.getNumber();
})