
// --- exception msgs ---
const NO_INPUT_MSG = "Text-area is empty";
const NO_PICK_MSG = "Type of graph is not selected";
const INVALID_INPUT_MSG = "Invalid input";


function validate_input(txt) {
    lines = txt.split("\n");

    for (let i = 0; i < lines.length; i++) {
        const line = lines[i];

        // Only one arrow is allowed
        const splitted = line.split("->");
        if (splitted.length > 2){
            return false;
        }

        // a comma on left side
        const from = splitted[0]
        if (from.includes(",")){
            return false;
        }

        const to = splitted[1];
        const wo_spaces = to.replace(" ", "");

        for (let j = 1; j < wo_spaces.length; j++) {
            if (wo_spaces.charAt(j) == ',' && wo_spaces.charAt(j - 1) == ',') {
                return false;
            }
        }
    }

    return true;
}


function getIm(e) {

    e.preventDefault();
    document.querySelector("#exception-msg").innerHTML = "";
    const user_input = this.querySelector("textarea").value;

    if (user_input == "") {
        document.querySelector("#exception-msg").innerHTML = NO_INPUT_MSG;
        return;
    }

    if (!validate_input(user_input)){
        document.querySelector("#exception-msg").innerHTML = INVALID_INPUT_MSG;
        return;
    };

    const im_width = document.querySelector("img").offsetWidth;
    const to_draw = document.querySelector('input[name="to-draw"]:checked');

    if (to_draw === null) {
        document.querySelector("#exception-msg").innerHTML = NO_PICK_MSG;
        return;
    }

    let formular = new URLSearchParams();
    formular.append('user-input', user_input);
    formular.append('im-width', im_width);
    formular.append('to-draw', to_draw.value);

    let url = this.action;
    let method = this.method;
    fetch(url, {method: method, body: formular})
        .then((res) => res.blob())
        .then((image) => {
            document.querySelector("#image-output").src = URL.createObjectURL(image);
        })

    // Submit 2nd form
    document.querySelector("#txt-button").click()
}


function getTxt(e) {

    e.preventDefault();

    const user_input = document.querySelector("textarea").value;
    const to_draw = document.querySelector('input[name="to-draw"]:checked').value;

    let formular = new URLSearchParams();
    formular.append('user-input', user_input);
    formular.append('to-draw', to_draw);

    let url = this.action;
    let method = this.method;
    fetch(url, {method: method, body: formular})
        .then((res) => res.blob())
        .then((solution) => {
            prom = solution.text()

            prom.then(
                function(result){
                    document.querySelector("#text-output").innerHTML = result;
            })
        })
} 

document.querySelector("#input-form").addEventListener("submit", getIm);
document.querySelector("#txt-form").addEventListener("submit", getTxt);
