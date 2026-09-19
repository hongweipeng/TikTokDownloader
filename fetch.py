from asyncio import CancelledError
from asyncio import run

from src.application import TikTokDownloader


async def main():
    async with TikTokDownloader() as downloader:
        try:
            downloader.project_info()
            downloader.check_config()
            await downloader.check_settings(
                False,
            )
            downloader.run_command = ['q', '1', '1']
            await downloader.complete()
        except (
                KeyboardInterrupt,
                CancelledError,
        ):
            return


if __name__ == "__main__":
    run(main())
