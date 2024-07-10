function submit_form() {
	form = document.getElementById("form_search_jornalista");
	form.submit();
}

function clear_input_name() {
	input_name = document.getElementById("input_nome");
	input_name.value = '';
}

search_icon = document.getElementById("icon_search");
search_icon.addEventListener("click", submit_form);

close_icon = document.getElementById("icon_close");
close_icon.addEventListener("click", clear_input_name);




