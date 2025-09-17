function isNan(a, b, c) {
  if (isNaN(a) || isNaN(b) || isNaN(c)) {
    console.log("Խնդրում եմ գրեք համապատասխանող թիվ");
    return true;
  }
  return false;
}

function checkNumber(a, b, c) {
  if (a === 0) {
    if (b === 0) {
      if (c === 0) {
        console.log("Լուծումը x ∈ (-∞, +∞)");
      } else {
        console.log("Լուծում չունի");
      }
    } else {
      let x = -c / b;
      console.log(`Պատասխան՝ x = ${x}`);
    }
  } else {
    const D = b ** 2 - 4 * a * c;
    calculateDiscriminant(a, b, c, D);
  }
}

function calculateDiscriminant(a, b, c, D) {
  if (D === 0) {
    let x = -b / (2 * a);
    console.log(`Մեկ կրկնվող լուծում՝ x = ${x}`);
  } else if (D > 0) {
    let x1 = (-b + Math.sqrt(D)) / (2 * a);
    let x2 = (-b - Math.sqrt(D)) / (2 * a);
    console.log(`Երկու լուծում՝ x₁ = ${x1}, x₂ = ${x2}`);
  } else {
    console.log("Լուծում չունի (բնական թվային լուծում չկա)");
  }
}

// Թեստերի զանգված
const testCases = [
  [1, 4, 2],     // D > 0
  [1, 4, 4],     // D = 0
  [3, 1, 4],     // D < 0
  [2, 4, 0],     // D > 0
  [4, 0, 4],     // D > 0
  [0, 4, 1],     // գծային
  [0, 0, 0],     // անորոշ
  [0, 0, 5],     // անհամատեղելի
];

// Կրկնվող հաշվարկներ
for (const [a, b, c] of testCases) {
  console.log(`\nԼուծում ${a}x² + ${b}x + ${c} = 0-ի համար`);
  if (!isNan(a, b, c)) {
    checkNumber(a, b, c);
  }
}

