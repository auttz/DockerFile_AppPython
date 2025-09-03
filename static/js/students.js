console.log("✅ students.js loaded");
$(document).ready(function() {
    // DataTables init
    $('#studentsTable').DataTable({
        "pageLength": 5,
        "lengthMenu": [5, 10, 25, 50, 100],
        "language": {
            "search": "ค้นหา:",
            "lengthMenu": "แสดง _MENU_ แถวต่อหน้า",
            "info": "แสดง _START_ ถึง _END_ จากทั้งหมด _TOTAL_ รายการ",
            "paginate": {
                "first": "หน้าแรก",
                "last": "หน้าสุดท้าย",
                "next": "ถัดไป",
                "previous": "ก่อนหน้า"
            }
        }
    });
    
    // Event ลบ row
    $(document).on("click", ".btn-delete", function() {
        let studentId = $(this).data("id");
        if (confirm("คุณต้องการลบข้อมูลนี้จริงหรือไม่?")) {
            fetch(`/delete/${studentId}`, {
                method: "POST"
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === "success") {
                    // ลบ row ออกจาก DataTable
                    let table = $('#studentsTable').DataTable();
                    table.row(`#row-${studentId}`).remove().draw();

                    alert("ลบข้อมูลเรียบร้อย!");
                }
            })
            .catch(err => console.error(err));
        }
    });
});
