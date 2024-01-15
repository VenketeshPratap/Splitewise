
document.addEventListener("DOMContentLoaded", function () {
    loadUsers();
    document.getElementById("splitType").addEventListener("change", handleSplitTypeChange);
    document.getElementById("addExpenseBtn").addEventListener("click", addExpense);
    document.getElementById("showBalancesBtn").addEventListener("click", showBalances);
});

function loadUsers() {
    const users = ["User1", "User2", "User3", "User4"];
    const paidBySelect = document.getElementById("paidBy");

    users.forEach(user => {
        const option = document.createElement("option");
        option.value = user;
        option.text = user;
        paidBySelect.add(option);
    });
}

function handleSplitTypeChange() {
    const splitType = document.getElementById("splitType").value;
    const splitOptionsDiv = document.getElementById("splitOptions");

    splitOptionsDiv.innerHTML = "";

    if (splitType === "EXACT" || splitType === "PERCENT") {
        const label = document.createElement("label");
        label.textContent = "Enter values (comma-separated):";

        const input = document.createElement("input");
        input.type = "text";
        input.name = "splitValues";
        input.required = true;

        splitOptionsDiv.appendChild(label);
        splitOptionsDiv.appendChild(input);
    }
}

function addExpense() {
    const form = document.getElementById("expenseForm");
    const formData = new FormData(form);

    fetch('/add_expense', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        // Display success or error message to the user
        alert(data.message);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function showBalances() {
    fetch('/show_balances')
    .then(response => response.json())
    .then(data => {
        updateBalanceUI(data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function updateBalanceUI(balances) {
    const balancesDiv = document.getElementById("balances");
    balancesDiv.innerHTML = "";

    for (const user in balances) {
        for (const debtor in balances[user]) {
            const amount = balances[user][debtor];
            const balanceText = `${debtor} owes ${user}: ${Math.abs(amount)}`;
            const balanceItem = document.createElement("div");
            balanceItem.textContent = balanceText;
            balancesDiv.appendChild(balanceItem);
        }
    }
}


function addUser() {
    const form = document.getElementById("userForm");
    const formData = new FormData(form);

    fetch('/add_user', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
