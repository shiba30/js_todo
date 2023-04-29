document.addEventListener("DOMContentLoaded", function () {
    const input = document.getElementById("inputText");
    const addButton = document.getElementById("addItemBtn");
    const list = document.getElementById("itemList");

    addButton.addEventListener("click", addToList);

    function addToList() {
        const text = input.value;
        if (!text) {
            // タスク未入力の場合
            return;
        }

        const newListItem = createNewListItem(text);
        if (newListItem) {
            list.appendChild(newListItem);
            updateTaskCounts();
        }
    }

    function createNewListItem(text) {
        const newListItem = document.createElement("li");
        newListItem.appendChild(createCheckBox());
        newListItem.appendChild(createTextSpan(text));
        newListItem.appendChild(createEditButton());
        newListItem.appendChild(createDeleteButton());

        // タスク入力後、入力欄を空白にする
        input.value = "";

        return newListItem;
    }

    function createCheckBox() {
        // チェックボックス作成
        const checkBox = document.createElement("input");
        checkBox.type = "checkbox";
        checkBox.className = "checkbox";
        checkBox.addEventListener("change", handleCheckBoxChange);
        return checkBox;
    }

    function handleCheckBoxChange(event) {
        // チェックボックス押下時
        const checkBox = event.target;
        const textSpan = checkBox.nextElementSibling;
        textStyles(checkBox, textSpan);
        updateTaskCounts();
    }

    function textStyles(checkBox, text) {
        // 取り消し線、背景グレー色を付与
        text.style.textDecoration = checkBox.checked ? "line-through" : "none";
        text.style.backgroundColor = checkBox.checked ? "rgb(221, 221, 229)" : "";
    }

    function createTextSpan(text) {
        // タスクテキスト作成
        const textSpan = document.createElement("span");
        textSpan.innerText = text;
        textSpan.className = "item-text";
        return textSpan;
    }

    function createEditButton() {
        // [編集]ボタン作成
        const editButton = document.createElement("button");
        editButton.innerText = "Edit";
        editButton.className = "edit-btn";
        editButton.addEventListener("click", handleEditButtonClick);
        return editButton;
    }

    function handleEditButtonClick(event) {
        // [編集]ボタン押下時処理
        const editButton = event.target;
        const listItem = editButton.parentElement;
        const textSpan = listItem.querySelector(".item-text");

        if (editButton.innerText === "Edit") {
            // 編集モードに切り替え
            listItem.replaceChild(createEditInput(textSpan.innerText), textSpan);
            editButton.innerText = "Save";
        } else {
            // 表示モードに切り替え
            const textSpan = document.createElement("span");
            textSpan.innerText = editButton.previousElementSibling.value;
            textSpan.className = "item-text";
            const checkBox = listItem.querySelector(".checkbox");
            textStyles(checkBox, textSpan);
            listItem.replaceChild(textSpan, editButton.previousElementSibling);
            editButton.innerText = "Edit";
        }
    }

    function createEditInput(value) {
        // [編集]ボタン作成
        const editInput = document.createElement("input");
        editInput.type = "text";
        editInput.className = "item-text";
        editInput.value = value;
        return editInput;
    }

    function createDeleteButton() {
        // [削除]ボタン作成
        const deleteButton = document.createElement("button");
        deleteButton.innerText = "Delete";
        deleteButton.className = "delete-btn";
        deleteButton.addEventListener("click", handleDeleteButtonClick);
        return deleteButton;
    }

    function handleDeleteButtonClick(event) {
        // [削除]ボタン押下時処理
        if (confirm("本当に削除してもよろしいですか？")) {
            const deleteButton = event.target;
            const listItem = deleteButton.parentElement;
            list.removeChild(listItem);
            updateTaskCounts();
        }
    }

    function updateTaskCounts() {
        // 全てのタスク、完了済み、未完了のタスク数を算出
        const totalCount = document.getElementById("total");
        const completedCount = document.getElementById("completed");
        const incompleteCount = document.getElementById("incomplete");

        const total = list.childElementCount;
        const completed = list.querySelectorAll('input[type="checkbox"]:checked').length;
        const incomplete = total - completed;

        totalCount.innerText = `全てのタスク：${total}`;
        completedCount.innerText = `完了済み：${completed}`;
        incompleteCount.innerText = `未完了：${incomplete}`;
    }

});
