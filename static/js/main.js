let contact_information = [
    {name:'valli',age:'19'},
    {name:'gardar',age:'24'}
]

let hrefVal = "";

function checkContact(){
    let fullName = document.getElementById("fullName").value;
    let streetName = document.getElementById("streetName").value;
    let houseNumber = document.getElementById("houseNumber").value;
    let country = document.getElementById("country").value;
    let city = document.getElementById("city").value;
    let postalCode = document.getElementById("postalCode").value;

    if (fullName === "") {
        document.getElementById("fullName").placeholder = "Must enter name";
    }
    console.log(fullName)
}

function checkHref() {
    console.log(hrefVal);
}