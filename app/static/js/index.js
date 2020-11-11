    <script type="text/javascript">
        function select_day(month) {
            switch(month) {
                        case "02":
                            end = 28;
                            break;
                        case "04": 
                        case "06":
                        case "09":
                        case "11":
                            end = 30;
                            break;
                        default:
                            end = 31;
                            break;
                    }
            
            document.getElementById('day_dependent').options.length = 0;

			var optn = document.createElement("OPTION");
			optn.text = '';
			optn.value = '';
            document.getElementById('day_dependent').options.add(optn)

            for (var i=1; i<=end; i++) {
                    var optn = document.createElement("OPTION");
                    i < 10 ? optn.text = '0' + i:optn.text = i 
                    i < 10 ? optn.value = '0' + i:optn.value = i 
                    document.getElementById('day_dependent').options.add(optn)
                }
            }
    </script>    
