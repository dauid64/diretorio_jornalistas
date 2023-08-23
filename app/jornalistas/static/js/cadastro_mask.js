$(function() {
    $('.mask-date').mask('00/00/0000');
    $('.mask-year').mask('0000');
    $('.mask-cpf').mask('000.000.000-00', {reverse: true});
    $('.mask-phone').mask('0000-0000');

    $('form').submit(function() {
        // Atualiza o valor do campo sem as mascaras
        $('.mask-cpf').unmask();
        $('.mask-phone').unmask();
    })
});