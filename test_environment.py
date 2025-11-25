# Check Package is working or not
def check_packageSklearn(packageSklearn):
    try:
        if packageSklearn == 'sklearn':
            import sklearn
            version = sklearn.__version__
        else:
            module = __import__(packageSklearn)
            version = module.__version__
        print(f"✅ {packageSklearn}: {version}")
        return True
    except ImportError:
        print(f"❌ {packageSklearn}: NOT AVAILABLE")
        return False

# Check core packages
packages = ['nltk', 'pandas', 'numpy']
all = all(check_packageSklearn(pkg) for pkg in packages)

print("=" * 50)
if all:
    print("ALL PACKAGES ARE WORKING!")
else:
    print("HERE ARE SOME MISSING PACKAGES.")

# Test NLTK functionality
try:
    import nltk
    from nltk.tokenize import word_tokenize
    test_text = "OPEC meeting about oil prices"
    tokens = word_tokenize(test_text)
    print(f" NLTK Tokenization: '{test_text}' → {tokens}")
except Exception as e:
    print(f" NLTK test failed: {e}")