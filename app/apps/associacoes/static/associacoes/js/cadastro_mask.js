$(function() {
    $('.mask-cnpj').mask('00.000.000/0000-00', {reverse: true});
    $('.mask-ddd').mask('(00)');
    $('.mask-telefone').mask('00000-0000');


    $('form').submit(function() {
        // Atualiza o valor do campo sem as mascaras
        $('.mask-cnpj').unmask();
        $('.mask-ddd').unmask();
        $('.mask-telefone').unmask();
    })
});