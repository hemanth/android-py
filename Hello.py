import android

droid = android.Android()
name = droid.getInput("Hello!", "What is your name?")
print name  # name is a namedtuple
droid.makeToast("Hello, %s" % name.result)
