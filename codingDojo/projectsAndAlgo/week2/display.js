display() {
    var listStr = "";
    if (this.head == null) {
        return "";
    }
    listStr += this.head.value;
    var runner = this.head.next;
    while (runner != null) {
        listStr += ", " + runner.value;
        runner = runner.next;
    }
    return listStr;
}