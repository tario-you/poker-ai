# List of your feature branches
FEATURE_BRANCHES=(
    "feature/abstraction-bet_sizing"
    "feature/abstraction-hands"
    "feature/abstraction-tree"
    "feature/engine-betting"
    "feature/engine-deck"
    "feature/engine-game"
    "feature/engine-hand_eval"
    "feature/engine-player"
    "feature/engine-state"
)

# Loop through each branch and pull from main
for branch in "${FEATURE_BRANCHES[@]}"
do
    git checkout "$branch"
    git pull origin "$branch"  # Ensure the branch is up to date
    git merge main  # Merge the latest changes from main
    git push origin "$branch"  # Push the merged updates
done