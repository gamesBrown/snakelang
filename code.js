num = 1
myArr = [1,2,3,4,5,6,7,8,9,10]


function binarySearch(arr,target){
    var ptr = arr.length/2;
    var i  = arr.length/2;

    while(arr[ptr] !== target)
    {
        console.log(i)
        i/=2
        
        if (arr[ptr] ===target){
            break
        }
        if (arr[ptr] >target){
            ptr-=Math.floor(i)
        }
        if (arr[ptr]<target){
            ptr+=Math.floor(i)
        }
        if (i <1){
            if (arr[ptr-1]=== target )
                return  ptr-1
            if (arr[ptr+1]===target)
                return ptr+1
            else{
                return -1
                }
        }
       
    if (arr[ptr] ===target){
        return ptr
    }
    }
       
        
}
        
console.log(binarySearch(myArr,num))
