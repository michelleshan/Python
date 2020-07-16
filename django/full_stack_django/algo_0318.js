function max_to_back(node){
    var runner = node, var max = node;
    while(runner != null){
        if(runner.val > max.val){
            max = runner;
        }
        runner = runner.next;
    }
    runner = node;
    while(runner != null){
        if(runner == max){
            head = runner.next;
            max.next = null;
            runner = head;
        }
        if(runner.next == max){
            runner.next = runner.next.next;
        }
        if(runner.next == null){
            runner.next = max;
            max.next = null;
        }
        runner = runner.next;
    }
    return head;
}
console.log(max_to_back(node))