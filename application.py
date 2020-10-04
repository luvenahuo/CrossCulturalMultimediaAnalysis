from datetime import datetime
from cca import app, db
from cca.models import Commits, Images, Affinity, Tags


@app.shell_context_processor
def make_shell_context():
    
    return {'db': db, 'Commits': Commits, 'Images': Images, 'Affinity':Affinity, 'Tags':Tags}
