$OutputFile = "data/raw/customers.csv"
$NumCustomers = 5000
$random = New-Object System.Random 42

# Create output directory if not exists
if (!(Test-Path "data/raw")) {
    New-Item -ItemType Directory -Path "data/raw" -Force | Out-Null
}

# Generate CSV header
$header = "customer_id,age,region,registration_date,total_purchases,total_value,avg_order_value,days_since_last_purchase,website_visits,email_opens,campaign_received,campaign_response,churn"

# Generate data rows
$rows = @($header)

for ($i = 1; $i -le $NumCustomers; $i++) {
    $customer_id = $i
    $age = $random.Next(18, 70)
    $regions = @("US", "EU", "ASIA", "OTHER")
    $region = $regions[$random.Next(0, 4)]
    
    # Random registration date in 2023
    $regDate = (Get-Date "2023-01-01").AddDays($random.Next(0, 365))
    $registration_date = $regDate.ToString("yyyy-MM-dd")
    
    # Exponential distribution approximation
    $total_purchases = [int]([Math]::Floor([Math]::Log($random.NextDouble()) * -5)) + 1
    $total_value = [int]([Math]::Floor([Math]::Log($random.NextDouble()) * -500))
    $avg_order_value = [Math]::Round($random.NextDouble() * 100 + 20, 2)
    $days_since = [int]([Math]::Floor([Math]::Log($random.NextDouble()) * -30))
    $website_visits = [int]([Math]::Floor([Math]::Log($random.NextDouble()) * -10))
    $email_opens = $random.Next(0, 20)
    $campaign_received = $random.Next(0, 10)
    $campaign_response = if ($random.NextDouble() -lt 0.15) { 1 } else { 0 }
    $churn = if ($random.NextDouble() -lt 0.16) { 1 } else { 0 }
    
    $row = "$customer_id,$age,$region,$registration_date,$total_purchases,$total_value,$avg_order_value,$days_since,$website_visits,$email_opens,$campaign_received,$campaign_response,$churn"
    $rows += $row
    
    if ($i % 500 -eq 0) {
        Write-Host "Generated $i customers..."
    }
}

# Write to CSV
$rows | Out-File -FilePath $OutputFile -Encoding UTF8

Write-Host "✅ Dataset created: $OutputFile"
Write-Host "   Records: $NumCustomers"

# Show sample
Write-Host "`n📊 Sample data:"
$rows[0..3] | ForEach-Object { Write-Host $_ }

Write-Host "`n✅ Ready for analysis!"
