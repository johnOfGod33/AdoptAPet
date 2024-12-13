const form = document.querySelector("form");

form.addEventListener("submit", (e) => validate_form(e));

/**
 *
 * @param {SubmitEvent} e
 */
const validate_form = (e) => {
  let isValid = true;

  document
    .querySelectorAll(".text-red-500")
    .forEach((el) => el.classList.add("hidden"));

  const nom = document.getElementById("nom").value.trim();
  const age = document.getElementById("age").value.trim();
  const espece = document.getElementById("espece").value.trim();
  const race = document.getElementById("race").value.trim();
  const courriel = document.getElementById("courriel").value.trim();
  const cp = document.getElementById("cp").value.trim();

  const regex = {
    nom: /^[^\s,]{3,20}$/, // Entre 3 et 20 caractères, sans virgule
    age: /^(?:[1-9]|[1-2][0-9]|30)$/, // Nombre entre 0 et 30
    espece: /^[^\s,]+$/, // Pas de virgule
    race: /^[^\s,]+$/, // Pas de virgule
    courriel: /^[^\s@]+@[^\s@]+\.[^\s@]+$/, // Email valide
    cp: /^[A-Za-z]\d[A-Za-z][ -]?\d[A-Za-z]\d$/, // Format postal canadien
  };

  if (!regex.nom.test(nom)) {
    isValid = false;
    const nomError = document.getElementById("error-nom");
    nomError.textContent =
      "Le nom doit contenir entre 3 et 20 caractères et ne pas inclure de virgule.";
    nomError.classList.remove("hidden");
    nomError.classList.add("block");
  }

  if (!regex.age.test(age)) {
    isValid = false;
    const ageError = document.getElementById("error-age");
    ageError.textContent = "L'âge doit être un nombre entre 0 et 30.";
    ageError.classList.remove("hidden");
    ageError.classList.add("block");
  }

  if (!regex.espece.test(espece)) {
    isValid = false;
    const especeError = document.getElementById("error-espece");
    especeError.textContent = "L'espèce ne doit pas inclure de virgule.";
    especeError.classList.remove("hidden");
    especeError.classList.add("block");
  }

  if (!regex.race.test(race)) {
    isValid = false;
    const raceError = document.getElementById("error-race");
    raceError.textContent = "La race ne doit pas inclure de virgule.";
    raceError.classList.remove("hidden");
    raceError.classList.add("block");
  }

  if (!regex.courriel.test(courriel)) {
    isValid = false;
    const courrielError = document.getElementById("error-courriel");
    courrielError.textContent = "Veuillez entrer un email valide.";
    courrielError.classList.remove("hidden");
    courrielError.classList.add("block");
  }

  if (!regex.cp.test(cp)) {
    isValid = false;
    const cpError = document.getElementById("error-cp");
    cpError.textContent =
      "Le code postal doit respecter le format canadien. (ex: K1A 0T6)";
    cpError.classList.remove("hidden");
    cpError.classList.add("block");
  }

  if (!isValid) {
    e.preventDefault();
  }
};

const errorPopup = document.getElementById("error-popup");
if (errorPopup) {
  setTimeout(() => {
    errorPopup.classList.add("opacity-0");
    setTimeout(() => errorPopup.remove(), 300);
  }, 3000);
}
