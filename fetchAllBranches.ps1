git branch -r | Where-Object { $_ -notmatch '->' } | ForEach-Object {
    $branch = $_.Trim() -replace 'origin/', ''
    git switch -c $branch "origin/$branch"
}
