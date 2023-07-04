function getDayOfTheWeek(i) {
    let arr = {
      1: "Mon",
      2: "Tue",
      3: "Wen", 
      4: "Thr",
      5: "Fri",
      6: "Sat",
      7: "Sun"
    }
    if (i > 0 && i < 7) {
      return arr[i];
    }
    return 0;
}

export function getTime() {
    let current = new Date()
    let curr_time =  getDayOfTheWeek(current.getDay()) + ", " + current.getHours() + ":" + current.getMinutes();
    return curr_time;
}