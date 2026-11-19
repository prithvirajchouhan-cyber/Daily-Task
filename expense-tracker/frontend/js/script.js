
// Backend API URL
const API_URL = "http://127.0.0.1:8000/api/v1/expenses/";

// Get HTML elements
const expenseForm = document.getElementById("expenseForm");
const expenseTableBody = document.getElementById("expenseTableBody");
const message = document.getElementById("message");
const submitButton = document.getElementById("submitButton");

// Store the ID of the expense being edited
let editingExpenseId = null;


// Show message on webpage
function showMessage(text, color = "green") {
    message.textContent = text;
    message.style.color = color;
}


// READ: Get all expenses from backend
async function getExpenses() {
    try {
        const response = await fetch(API_URL);

        if (!response.ok) {
            throw new Error("Unable to fetch expenses");
        }

        const result = await response.json();

        displayExpenses(result.data);

    } catch (error) {
        showMessage(error.message, "red");
    }
}


// Display expenses in HTML table
function displayExpenses(expenses) {

    expenseTableBody.innerHTML = "";

    if (expenses.length === 0) {
        expenseTableBody.innerHTML = `
            <tr>
                <td colspan="6">No expenses found</td>
            </tr>
        `;
        return;
    }

    expenses.forEach(expense => {

        const row = document.createElement("tr");

        const values = [
            expense.id,
            expense.title,
            `₹${expense.amount}`,
            expense.category,
            expense.expense_date
        ];

        values.forEach(value => {
            const cell = document.createElement("td");
            cell.textContent = value;
            row.appendChild(cell);
        });

        // Create action buttons
        const actionCell = document.createElement("td");

        const editButton = document.createElement("button");
        editButton.textContent = "Edit";
        editButton.type = "button";
        editButton.style.marginRight = "5px";
        editButton.onclick = () => editExpense(expense);

        const deleteButton = document.createElement("button");
        deleteButton.textContent = "Delete";
        deleteButton.type = "button";
        deleteButton.style.backgroundColor = "#dc2626";
        deleteButton.onclick = () => deleteExpense(expense.id);

        actionCell.appendChild(editButton);
        actionCell.appendChild(deleteButton);

        row.appendChild(actionCell);

        expenseTableBody.appendChild(row);
    });
}


// CREATE and UPDATE: Handle form submission
expenseForm.addEventListener("submit", async function(event) {

    event.preventDefault();

    // Get values from form
    const expenseData = {
        title: document.getElementById("title").value.trim(),
        amount: parseFloat(document.getElementById("amount").value),
        category: document.getElementById("category").value,
        expense_date: document.getElementById("expense_date").value
    };

    try {

        let url = API_URL;
        let method = "POST";

        // If editing, use PUT
        if (editingExpenseId !== null) {
            url = API_URL + editingExpenseId;
            method = "PUT";
        }

        const response = await fetch(url, {
            method: method,
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(expenseData)
        });

        const result = await response.json();

        if (!response.ok) {
            throw new Error(result.detail || "Something went wrong");
        }

        showMessage(result.message);

        // Reset form after success
        expenseForm.reset();
        editingExpenseId = null;
        submitButton.textContent = "Add Expense";

        // Refresh expense list
        getExpenses();

    } catch (error) {
        showMessage(error.message, "red");
    }
});


// Load selected expense into form for editing
function editExpense(expense) {

    document.getElementById("title").value = expense.title;
    document.getElementById("amount").value = expense.amount;
    document.getElementById("category").value = expense.category;
    document.getElementById("expense_date").value = expense.expense_date;

    editingExpenseId = expense.id;

    submitButton.textContent = "Update Expense";

    showMessage("Editing expense ID: " + expense.id, "blue");
}


// DELETE: Remove an expense
async function deleteExpense(expenseId) {

    const confirmed = confirm("Are you sure you want to delete this expense?");

    if (!confirmed) {
        return;
    }

    try {

        const response = await fetch(API_URL + expenseId, {
            method: "DELETE"
        });

        const result = await response.json();

        if (!response.ok) {
            throw new Error(result.detail || "Unable to delete expense");
        }

        showMessage(result.message);

        // Refresh table
        getExpenses();

    } catch (error) {
        showMessage(error.message, "red");
    }
}


// Load expenses when webpage opens
getExpenses();
