const studentName = document.getElementById("studentName");
const lucId = document.getElementById("lucId");
const lucMail = document.getElementById("lucEmail");
const description = document.getElementByID("description");
const category = document.getElementById("category");


let information = []



const submitBtn = document.getElementById("submitBtn");

submitBtn.addEventListener("click", function () {



    const student = {
        sName: studentName.value,
        sId: lucId.value,
        sEmail: lucMail.value,
        description: description.value,
        category: category.value
    };


    submissions.push(student);

    localStorage, setItem("submissions", JSON.stringify(submissions));
});


