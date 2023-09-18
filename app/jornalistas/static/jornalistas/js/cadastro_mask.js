$(function() {
    $('.mask-cpf').mask('000.000.000-00', {reverse: true});

    $('form').submit(function() {
        // Atualiza o valor do campo sem as mascaras
        $('.mask-cpf').unmask();
    })
});