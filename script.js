// Loan Calculator
document.getElementById('loanCalc')?.addEventListener('submit', function(e) {
    e.preventDefault();
    const commodity = document.getElementById('commodity').value;
    const quantity = parseFloat(document.getElementById('quantity').value);
    const price = parseFloat(document.getElementById('price').value);
    const loan = quantity * price * 0.8; // 80% of value as loan
    const resultElement = document.getElementById('loanResult');
    resultElement.textContent = `Estimated Loan: ₹${loan.toFixed(2)}`;
    resultElement.classList.add('result-fade-in');
    setTimeout(() => resultElement.classList.remove('result-fade-in'), 500);
});

// Complaint Form
document.getElementById('complaintForm')?.addEventListener('submit', function(e) {
    e.preventDefault();
    const name = document.getElementById('name').value;
    const issue = document.getElementById('issue').value;
    const description = document.getElementById('description').value;
    document.getElementById('complaintMsg').textContent = `Complaint submitted by ${name} for ${issue}.`;
    this.reset();
});

// Volunteer Form
document.getElementById('volunteerForm')?.addEventListener('submit', function(e) {
    e.preventDefault();
    const vname = document.getElementById('vname').value;
    const expertise = document.getElementById('expertise').value;
    const contact = document.getElementById('contact').value;
    document.getElementById('volunteerMsg').textContent = `Volunteer ${vname} enrolled as ${expertise}.`;
    this.reset();
});

// Loan Page Functions
function scrollToLoanCalculator() {
    const element = document.getElementById('loanCalculator');
    element.scrollIntoView({ behavior: 'smooth' });
    // Add click animation to the option
    const option = document.querySelector('.loan-option[onclick*="scrollToLoanCalculator"]');
    option.classList.add('clicked');
    setTimeout(() => option.classList.remove('clicked'), 300);
}

function openEmergencyModal() {
    const modal = document.getElementById('emergencyModal');
    modal.style.display = 'block';
    // Add click animation to the option
    const option = document.querySelector('.loan-option[onclick*="openEmergencyModal"]');
    option.classList.add('clicked');
    setTimeout(() => option.classList.remove('clicked'), 300);
}

function closeEmergencyModal() {
    document.getElementById('emergencyModal').style.display = 'none';
}

function toggleCropLoanInfo() {
    const expandable = document.getElementById('cropLoanInfo');
    expandable.classList.toggle('open');
    // Add click animation to the option
    const option = document.querySelector('.loan-option[onclick*="toggleCropLoanInfo"]');
    option.classList.add('clicked');
    setTimeout(() => option.classList.remove('clicked'), 300);
}

function toggleCropGuidance() {
    const expandable = document.getElementById('cropGuidance');
    expandable.classList.toggle('open');
    // Add click animation to the option
    const option = document.querySelector('.loan-option[onclick*="toggleCropGuidance"]');
    option.classList.add('clicked');
    setTimeout(() => option.classList.remove('clicked'), 300);
}

function toggleModernFarming() {
    const expandable = document.getElementById('modernFarming');
    expandable.classList.toggle('open');
    // Add click animation to the option
    const option = document.querySelector('.loan-option[onclick*="toggleModernFarming"]');
    option.classList.add('clicked');
    setTimeout(() => option.classList.remove('clicked'), 300);
}

function toggleFinancialEducation() {
    const expandable = document.getElementById('financialEducation');
    expandable.classList.toggle('open');
    // Add click animation to the option
    const option = document.querySelector('.loan-option[onclick*="toggleFinancialEducation"]');
    option.classList.add('clicked');
    setTimeout(() => option.classList.remove('clicked'), 300);
}

// Enhanced redirect with fade-out
function redirectWithFade(url) {
    const body = document.body;
    body.classList.add('fade-out');
    setTimeout(() => {
        window.location.href = url;
    }, 500);
    // Add click animation to the option
    const option = document.querySelector('.loan-option[onclick*="redirectWithFade"]');
    if (option) {
        option.classList.add('clicked');
        setTimeout(() => option.classList.remove('clicked'), 300);
    }
}

// Education Section Toggle
function toggleSection(sectionId) {
    const content = document.getElementById(sectionId);
    content.classList.toggle('open');
}

// Close modal when clicking outside
window.onclick = function(event) {
    const modal = document.getElementById('emergencyModal');
    if (event.target == modal) {
        modal.style.display = 'none';
    }
}
