const fs=require('fs');

fs.writeFileSync("naman.txt","Naman is a good boy")

fs.writeFile("naman2.txt","Naman is a good boy2", () => {
    console.log("File created successfully 2nd");
    fs.readFile("naman2.txt", (err, data) => {
        if (err) {
            console.error("Error reading file:", err);
        } else {
            console.log("File content:", data.toString());
        } 
    });
})
console.log("File created successfully 1st");