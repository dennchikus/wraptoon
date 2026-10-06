/**
 * WRAP TOON — Автокомплит популярных марок и моделей авто
 * Легковесный скрипт (~6 КБ), фильтрация на лету, поддержка синонимов и кириллицы.
 */

const POPULAR_CARS = [
  // BMW
  "BMW 1 серии (F20/F40)",
  "BMW 2 серии / Gran Coupe",
  "BMW 3 серии (G20/F30)",
  "BMW 4 серии (G22/F32)",
  "BMW 5 серии (G30/G60/F10)",
  "BMW 6 серии GT",
  "BMW 7 серии (G11/G70)",
  "BMW 8 серии (G15)",
  "BMW X1 / X2",
  "BMW X3 (G01)",
  "BMW X4 (G02)",
  "BMW X5 (G05/F15)",
  "BMW X6 (G06/F16)",
  "BMW X7 (G07)",
  "BMW M3 / M4",
  "BMW M5 (F90)",
  "BMW M8",
  "BMW XM",

  // Mercedes-Benz
  "Mercedes-Benz A-Class",
  "Mercedes-Benz CLA / CLS",
  "Mercedes-Benz C-Class (W205/W206)",
  "Mercedes-Benz E-Class (W213/W214)",
  "Mercedes-Benz S-Class (W222/W223)",
  "Mercedes-Benz GLA / GLB",
  "Mercedes-Benz GLC / GLC Coupe",
  "Mercedes-Benz GLE / GLE Coupe",
  "Mercedes-Benz GLS / Maybach",
  "Mercedes-Benz G-Class (Гелендваген)",
  "Mercedes-Benz AMG GT",

  // Audi
  "Audi A3 / S3",
  "Audi A4 / A5",
  "Audi A6 / A7 (C8)",
  "Audi A8 (D5)",
  "Audi Q3",
  "Audi Q5",
  "Audi Q7",
  "Audi Q8 / SQ8 / RS Q8",
  "Audi RS6 Avant",
  "Audi e-tron / GT",

  // Porsche
  "Porsche Cayenne / Coupe",
  "Porsche Macan",
  "Porsche Panamera",
  "Porsche 911 (992)",
  "Porsche Taycan",
  "Porsche Boxster / Cayman",

  // Geely
  "Geely Monjaro",
  "Geely Coolray",
  "Geely Tugella",
  "Geely Atlas / Atlas Pro",
  "Geely Preface",
  "Geely Emgrand",
  "Geely Okavango",

  // Haval & Tank
  "Haval Jolion",
  "Haval F7 / F7x",
  "Haval Dargo",
  "Haval H9",
  "Haval M6",
  "Tank 300",
  "Tank 500",

  // Chery, Exeed, Omoda, Jaecoo
  "Chery Tiggo 4 / 4 Pro",
  "Chery Tiggo 7 Pro / Max",
  "Chery Tiggo 8 Pro / Max",
  "Chery Arrizo 8",
  "Exeed RX",
  "Exeed TXL",
  "Exeed VX",
  "Exeed LX",
  "Omoda C5",
  "Omoda S5",
  "Jaecoo J7",
  "Jaecoo J8",

  // Changan
  "Changan UNI-V",
  "Changan UNI-K",
  "Changan UNI-T",
  "Changan CS35 Plus",
  "Changan CS55 Plus",
  "Changan CS75 Plus",
  "Changan CS95",

  // Zeekr, Li Auto, Voyah
  "Li Auto L7",
  "Li Auto L8",
  "Li Auto L9",
  "Zeekr 001 / FR",
  "Zeekr 007",
  "Zeekr 009",
  "Zeekr X",
  "Voyah Free",
  "Voyah Dream",
  "Voyah Passion",
  "Avatr 11 / 12",

  // Toyota & Lexus
  "Toyota Camry (XV70/XV80)",
  "Toyota RAV4 (XA50)",
  "Toyota Land Cruiser Prado 150/250",
  "Toyota Land Cruiser 200 / 300",
  "Toyota Corolla",
  "Toyota Highlander",
  "Toyota Alphard",
  "Toyota Hilux",
  "Lexus RX 300/350/500h",
  "Lexus NX 200/250/350",
  "Lexus LX 570 / 600",
  "Lexus ES 200/250/350",
  "Lexus GX 460 / 550",

  // LADA
  "LADA Vesta / Vesta SW Cross",
  "LADA Granta",
  "LADA Niva Legend",
  "LADA Niva Travel",
  "LADA Largus",

  // Kia & Hyundai & Genesis
  "Kia K5",
  "Kia Rio / Rio X-Line",
  "Kia Sportage",
  "Kia Sorento",
  "Kia Carnival",
  "Kia Stinger",
  "Kia Cerato / Ceed",
  "Kia Seltos",
  "Hyundai Solaris",
  "Hyundai Sonata",
  "Hyundai Elantra",
  "Hyundai Tucson",
  "Hyundai Santa Fe",
  "Hyundai Palisade",
  "Hyundai Staria",
  "Genesis G70 / G80",
  "Genesis GV70 / GV80",

  // Volkswagen & Skoda
  "Volkswagen Polo",
  "Volkswagen Tiguan",
  "Volkswagen Touareg",
  "Volkswagen Golf / GTI",
  "Volkswagen Passat",
  "Volkswagen Teramont",
  "Skoda Octavia (A7/A8)",
  "Skoda Rapid",
  "Skoda Kodiaq",
  "Skoda Superb",
  "Skoda Karoq",

  // Другие популярные
  "Tesla Model 3",
  "Tesla Model Y",
  "Tesla Model S / Plaid",
  "Tesla Model X",
  "Ford Focus",
  "Ford Mondeo",
  "Ford Mustang",
  "Ford Explorer",
  "Mazda 3",
  "Mazda 6",
  "Mazda CX-5",
  "Mazda CX-9",
  "Nissan Qashqai",
  "Nissan X-Trail",
  "Nissan Teana",
  "Nissan Patrol",
  "Subaru Forester",
  "Subaru Outback",
  "Subaru WRX / STI",
  "Land Rover Defender",
  "Land Rover Range Rover / Sport / Velar"
];

// Синонимы для поиска брендов на русском языке
const BRAND_SYNONYMS = {
  "бмв": "bmw",
  "мерс": "mercedes",
  "мерседес": "mercedes",
  "мерин": "mercedes",
  "ауди": "audi",
  "порш": "porsche",
  "порше": "porsche",
  "фолькс": "volkswagen",
  "фольксваген": "volkswagen",
  "ваг": "volkswagen",
  "шкода": "skoda",
  "октавия": "octavia",
  "тойота": "toyota",
  "таёта": "toyota",
  "камри": "camry",
  "крузак": "land cruiser",
  "прадо": "prado",
  "лексус": "lexus",
  "лада": "lada",
  "ваз": "lada",
  "гранта": "granta",
  "веста": "vesta",
  "нива": "niva",
  "киа": "kia",
  "кия": "kia",
  "хендай": "hyundai",
  "хёндай": "hyundai",
  "солярис": "solaris",
  "генезис": "genesis",
  "джили": "geely",
  "монжаро": "monjaro",
  "кулрей": "coolray",
  "тугелла": "tugella",
  "хавал": "haval",
  "джолион": "jolion",
  "дарго": "dargo",
  "чери": "chery",
  "тигго": "tiggo",
  "эксид": "exeed",
  "омода": "omoda",
  "чанган": "changan",
  "юни": "uni",
  "танк": "tank",
  "зикр": "zeekr",
  "зикер": "zeekr",
  "ли": "li auto",
  "лисян": "li auto",
  "воя": "voyah",
  "тесла": "tesla",
  "мазда": "mazda",
  "ниссан": "nissan",
  "субару": "subaru",
  "форд": "ford"
};

/**
 * Инициализирует автокомплит для поля ввода автомобиля
 * @param {HTMLInputElement} inputEl
 */
function initCarAutocomplete(inputEl) {
  if (!inputEl || inputEl.dataset.autocompleteAttached) return;
  inputEl.dataset.autocompleteAttached = "true";

  // Оборачиваем input в relative-контейнер, если еще не обернут
  let wrapper = inputEl.parentElement;
  if (!wrapper.classList.contains("toon-autocomplete-wrapper")) {
    wrapper = document.createElement("div");
    wrapper.className = "toon-autocomplete-wrapper";
    inputEl.parentNode.insertBefore(wrapper, inputEl);
    wrapper.appendChild(inputEl);
  }

  // Создаем выпадающий список
  const dropdown = document.createElement("ul");
  dropdown.className = "toon-autocomplete-dropdown";
  wrapper.appendChild(dropdown);

  let activeIndex = -1;
  let currentMatches = [];

  function closeDropdown() {
    dropdown.classList.remove("is-open");
    dropdown.innerHTML = "";
    activeIndex = -1;
    currentMatches = [];
  }

  function highlightMatch(text, query) {
    if (!query) return text;
    const lowerText = text.toLowerCase();
    const lowerQuery = query.toLowerCase();
    const idx = lowerText.indexOf(lowerQuery);
    if (idx === -1) return text;
    return (
      text.substring(0, idx) +
      `<span class="match-highlight">${text.substring(idx, idx + query.length)}</span>` +
      text.substring(idx + query.length)
    );
  }

  function renderMatches(query) {
    const trimmed = query.trim().toLowerCase();
    if (trimmed.length < 1) {
      closeDropdown();
      return;
    }

    // Проверяем синонимы марок
    let searchKey = trimmed;
    for (const [rusWord, engWord] of Object.entries(BRAND_SYNONYMS)) {
      if (trimmed.startsWith(rusWord) || trimmed === rusWord) {
        searchKey = trimmed.replace(rusWord, engWord);
        break;
      }
    }

    currentMatches = POPULAR_CARS.filter(car => {
      const lowerCar = car.toLowerCase();
      return lowerCar.includes(trimmed) || lowerCar.includes(searchKey);
    }).slice(0, 7); // Топ-7 подсказок

    dropdown.innerHTML = "";
    activeIndex = -1;

    if (currentMatches.length === 0) {
      closeDropdown();
      return;
    }

    currentMatches.forEach((carName, idx) => {
      const li = document.createElement("li");
      li.className = "toon-autocomplete-item";
      li.dataset.index = idx;

      // Иконка машинки + подсвеченный текст
      const displayHighlight = trimmed.length >= 2 ? trimmed : (searchKey.length >= 2 ? searchKey : "");
      li.innerHTML = `<span>🏎</span><span>${highlightMatch(carName, displayHighlight)}</span>`;

      li.addEventListener("mousedown", (e) => {
        // mousedown вместо click, чтобы не сработал blur инпута
        e.preventDefault();
        inputEl.value = carName;
        inputEl.dispatchEvent(new Event("change", { bubbles: true }));
        closeDropdown();
      });

      dropdown.appendChild(li);
    });

    dropdown.classList.add("is-open");
  }

  function updateActiveItem() {
    const items = dropdown.querySelectorAll(".toon-autocomplete-item");
    items.forEach((item, idx) => {
      if (idx === activeIndex) {
        item.classList.add("is-active");
        item.scrollIntoView({ block: "nearest" });
      } else {
        item.classList.remove("is-active");
      }
    });
  }

  // Слушатель ввода
  inputEl.addEventListener("input", (e) => {
    renderMatches(e.target.value);
  });

  // Фокус: если уже что-то введено, показываем список
  inputEl.addEventListener("focus", (e) => {
    if (e.target.value.trim().length >= 1) {
      renderMatches(e.target.value);
    }
  });

  // Клавиатурная навигация
  inputEl.addEventListener("keydown", (e) => {
    if (!dropdown.classList.contains("is-open")) return;

    if (e.key === "ArrowDown") {
      e.preventDefault();
      activeIndex = (activeIndex + 1) % currentMatches.length;
      updateActiveItem();
    } else if (e.key === "ArrowUp") {
      e.preventDefault();
      activeIndex = (activeIndex - 1 + currentMatches.length) % currentMatches.length;
      updateActiveItem();
    } else if (e.key === "Enter") {
      if (activeIndex >= 0 && activeIndex < currentMatches.length) {
        e.preventDefault();
        inputEl.value = currentMatches[activeIndex];
        inputEl.dispatchEvent(new Event("change", { bubbles: true }));
        closeDropdown();
      }
    } else if (e.key === "Escape") {
      closeDropdown();
    }
  });

  // Закрытие при клике вне поля
  document.addEventListener("click", (e) => {
    if (!wrapper.contains(e.target)) {
      closeDropdown();
    }
  });
}

// Автоматическая инициализация всех подходящих полей на странице
document.addEventListener("DOMContentLoaded", () => {
  const targetInputs = [
    document.getElementById("client-car"),
    document.getElementById("consult-car")
  ];

  targetInputs.forEach(input => {
    if (input) initCarAutocomplete(input);
  });
});
