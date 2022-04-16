$(document).ready(function(){

var items = ["Air Pods","Apple Pencil", "Wallet - Lether", "Wallet - Trifold","Aggie Card","Passport","Key","Debit Card","Credit Card","Tablet","Driver's License"];

  $("#tags").autocomplete({
    source: items
});
});
