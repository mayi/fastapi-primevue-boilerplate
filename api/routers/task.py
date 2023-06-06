from fastapi import APIRouter, Depends, HTTPException, status
from aps import scheduler


router = APIRouter(
    prefix="/api/task",
    tags=["task"],
)

# start the scheduler
@router.get("/start")
async def start():
    scheduler.start()
    return {"message": "scheduler started!"}

# pause the scheduler
@router.get("/pause")
async def pause():
    scheduler.pause()
    return {"message": "scheduler paused!"}

# resume the scheduler
@router.get("/resume")
async def resume():
    scheduler.resume()
    return {"message": "scheduler resumed!"}

# shutdown the scheduler
@router.get("/shutdown")
async def shutdown():
    scheduler.shutdown()
    return {"message": "scheduler shutdown!"}

# get the scheduler status
@router.get("/status")
async def status():
    return {"message": scheduler.state}

# get the scheduler jobs
@router.get("/jobs")
async def jobs():
    return {"message": scheduler.get_jobs()}

# get the scheduler job
@router.get("/job/{job_id}")
async def job(job_id: str):
    return {"message": scheduler.get_job(job_id=job_id)}

# add a job to the scheduler
@router.post("/add")
async def add_job(job_id: str, job_func: str, trigger: str, **trigger_args):
    try:
        scheduler.add_job(id=job_id, func=job_func, trigger=trigger, **trigger_args)
        return {"message": "job added!"}
    except Exception as e:
        return {"message": str(e)}

# modify a job in the scheduler
@router.post("/modify/{job_id}")
async def modify_job(job_id: str, job_func: str, trigger: str, **trigger_args):
    try:
        scheduler.modify_job(id=job_id, func=job_func, trigger=trigger, **trigger_args)
        return {"message": "job modified!"}
    except Exception as e:
        return {"message": str(e)}

# remove a job from the scheduler
@router.post("/remove/{job_id}")
async def remove_job(job_id: str):
    try:
        scheduler.remove_job(id=job_id)
        return {"message": "job removed!"}
    except Exception as e:
        return {"message": str(e)}

# pause a job in the scheduler
@router.post("/pause/{job_id}")
async def pause_job(job_id: str):
    try:
        scheduler.pause_job(id=job_id)
        return {"message": "job paused!"}
    except Exception as e:
        return {"message": str(e)}

# resume a job in the scheduler
@router.post("/resume/{job_id}")
async def resume_job(job_id: str):
    try:
        scheduler.resume_job(id=job_id)
        return {"message": "job resumed!"}
    except Exception as e:
        return {"message": str(e)}

# run a job in the scheduler
@router.post("/run/{job_id}")
async def run_job(job_id: str):
    try:
        scheduler.run_job(id=job_id)
        return {"message": "job run!"}
    except Exception as e:
        return {"message": str(e)}

