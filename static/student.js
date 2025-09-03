// static/js/students.js
$(document).ready(function() {
    $('#studentsTable').DataTable({
        "pageLength": 5,          // ✅ แสดง 5 แถวต่อหน้า
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
});
